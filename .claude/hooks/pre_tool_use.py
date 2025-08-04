#!/usr/bin/env python3
"""
Pre-tool use hook for Claude Code Template
Provides security safeguards and enhanced logging for tool usage.
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, Any


class SecurityChecker:
    """Handles security checks for tool usage."""
    
    DANGEROUS_RM_PATTERNS = [
        r'\brm\s+.*-[a-z]*r[a-z]*f',
        r'\brm\s+.*-[a-z]*f[a-z]*r',
        r'\brm\s+--recursive\s+--force',
        r'\brm\s+--force\s+--recursive',
        r'\brm\s+-r\s+.*-f',
        r'\brm\s+-f\s+.*-r'
    ]
    
    DANGEROUS_PATHS = [
        r'/',
        r'/\*',
        r'~',
        r'~/',
        r'\$HOME',
        r'\.\.',
        r'\*',
        r'\.',
        r'\.\s*$'
    ]
    
    ENV_FILE_PATTERNS = [
        r'\.env\b(?!\.sample)',
        r'cat\s+.*\.env\b(?!\.sample)',
        r'echo\s+.*>\s*\.env\b(?!\.sample)',
        r'touch\s+.*\.env\b(?!\.sample)',
        r'cp\s+.*\.env\b(?!\.sample)',
        r'mv\s+.*\.env\b(?!\.sample)'
    ]
    
    def is_dangerous_rm_command(self, command: str) -> bool:
        """Check if command contains dangerous rm operations."""
        normalized = command.lower().strip()
        
        # Check for dangerous rm patterns
        for pattern in self.DANGEROUS_RM_PATTERNS:
            if re.search(pattern, normalized):
                return True
        
        # Check for rm with recursive flag targeting dangerous paths
        if re.search(r'\brm\s+.*-[a-z]*r', normalized):
            for path in self.DANGEROUS_PATHS:
                if re.search(path, normalized):
                    return True
        
        return False
    
    def is_env_file_access(self, tool_name: str, tool_input: Dict[str, Any]) -> bool:
        """Check if tool is accessing .env files."""
        if tool_name in ["Read", "Edit", "MultiEdit", "Write"]:
            file_path = tool_input.get("file_path", "")
            if ".env" in file_path and ".env.sample" not in file_path:
                return True
        
        elif tool_name == "Bash":
            command = tool_input.get("command", "")
            for pattern in self.ENV_FILE_PATTERNS:
                if re.search(pattern, command):
                    return True
        
        return False


class HookLogger:
    """Handles logging of tool usage data."""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.log_path = self.log_dir / "pre_tool_use.json"
    
    def log_tool_usage(self, data: Dict[str, Any]) -> None:
        """Log tool usage data to JSON file."""
        try:
            # Read existing log data
            log_data = []
            if self.log_path.exists():
                try:
                    with open(self.log_path, 'r') as f:
                        log_data = json.load(f)
                except (json.JSONDecodeError, IOError):
                    log_data = []
            
            # Append new data
            log_data.append(data)
            
            # Write back to file
            with open(self.log_path, 'w') as f:
                json.dump(log_data, f, indent=2)
                
        except Exception as e:
            # Log errors to stderr but don't fail the hook
            print(f"Warning: Failed to log tool usage: {e}", file=sys.stderr)


def main():
    """Main hook execution function."""
    try:
        # Read JSON input from stdin
        input_data = sys.stdin.read().strip()
        if not input_data:
            sys.exit(0)
        
        # Parse JSON input
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            sys.exit(0)  # Gracefully handle JSON errors
        
        # Extract tool information
        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})
        
        # Initialize security checker
        security = SecurityChecker()
        
        # Check for .env file access
        if security.is_env_file_access(tool_name, tool_input):
            print("BLOCKED: Access to .env files containing sensitive data is prohibited", file=sys.stderr)
            print("Use .env.sample for template files instead", file=sys.stderr)
            sys.exit(2)  # Exit code 2 blocks tool call and shows error
        
        # Check for dangerous rm commands
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            if security.is_dangerous_rm_command(command):
                print("BLOCKED: Dangerous rm command detected and prevented", file=sys.stderr)
                sys.exit(2)  # Exit code 2 blocks tool call and shows error
        
        # Log tool usage
        logger = HookLogger()
        logger.log_tool_usage(data)
        
        # Success
        sys.exit(0)
        
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"Hook error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't block tool execution for unexpected errors


if __name__ == "__main__":
    main()