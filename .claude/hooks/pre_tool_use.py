#!/usr/bin/env python3
"""
Balanced pre-tool use hook for Claude Code
Provides warnings and guidance rather than hard blocks, with configuration options.
"""

import json
import sys
import re
import os
from pathlib import Path
from typing import Dict, Any, Optional


class BalancedSecurityChecker:
    """Provides security guidance with configurable restrictions."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration with defaults."""
        default_config = {
            "block_env_access": False,  # Warn instead of block
            "block_dangerous_rm": True,  # Still block truly dangerous operations
            "allow_project_cleanup": True,  # Allow common project cleanup operations
            "warning_mode": True,  # Show warnings for risky operations
            "safe_rm_patterns": [
                r"node_modules/?$",
                r"\.cache/?$", 
                r"dist/?$",
                r"build/?$",
                r"\*\.tmp$",
                r"\*\.log$",
                r"__pycache__/?$"
            ],
            "truly_dangerous_paths": [
                r"^/$",  # Root directory
                r"^/usr",
                r"^/etc",
                r"^/var(?!/tmp)",
                r"^/home$",
                r"^/Users$",
                r"^\*$",  # Everything wildcard
                r"^\.$"  # Current directory without subdirectory
            ]
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                default_config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass  # Use defaults if config is invalid
        
        return default_config
    
    def check_rm_command(self, command: str) -> tuple[bool, str]:
        """Check rm command and return (should_block, message)."""
        normalized = command.lower().strip()
        
        # Check if it's a recursive rm
        if not re.search(r'\brm\s+.*-[a-z]*r', normalized):
            return False, ""  # Non-recursive rm is generally safe
        
        # Extract the target path(s)
        rm_match = re.search(r'\brm\s+[^/\w]*([^\s]+(?:\s+[^\s]+)*)', command)
        if not rm_match:
            return False, ""
        
        targets = rm_match.group(1)
        
        # Check for truly dangerous patterns
        for dangerous_pattern in self.config["truly_dangerous_paths"]:
            if re.search(dangerous_pattern, targets):
                return True, f"BLOCKED: Attempting to recursively delete critical system path: {targets}"
        
        # Check for safe project cleanup patterns
        if self.config["allow_project_cleanup"]:
            for safe_pattern in self.config["safe_rm_patterns"]:
                if re.search(safe_pattern, targets):
                    if self.config["warning_mode"]:
                        print(f"⚠️  Warning: Removing {targets} - this appears to be project cleanup", file=sys.stderr)
                    return False, ""
        
        # For other recursive rm operations, warn but don't block
        if self.config["warning_mode"]:
            print(f"⚠️  Warning: Recursive rm operation on {targets} - please confirm this is intentional", file=sys.stderr)
        
        return False, ""
    
    def check_env_file_access(self, tool_name: str, tool_input: Dict[str, Any]) -> tuple[bool, str]:
        """Check .env file access and return (should_block, message)."""
        if not self._is_env_access(tool_name, tool_input):
            return False, ""
        
        if self.config["block_env_access"]:
            return True, "BLOCKED: Direct .env file access is restricted. Use .env.example for templates."
        
        if self.config["warning_mode"]:
            print("⚠️  Warning: Accessing .env file containing sensitive data", file=sys.stderr)
            print("💡 Tip: Consider using .env.example for sharing configuration templates", file=sys.stderr)
        
        return False, ""
    
    def _is_env_access(self, tool_name: str, tool_input: Dict[str, Any]) -> bool:
        """Check if operation accesses .env files."""
        if tool_name in ["Read", "Edit", "MultiEdit", "Write"]:
            file_path = tool_input.get("file_path", "")
            return ".env" in file_path and ".env.sample" not in file_path and ".env.example" not in file_path
        
        elif tool_name == "Bash":
            command = tool_input.get("command", "")
            env_patterns = [
                r'cat\s+.*\.env\b(?!\.sample|\.example)',
                r'echo\s+.*>\s*\.env\b(?!\.sample|\.example)',
                r'touch\s+.*\.env\b(?!\.sample|\.example)',
                r'cp\s+.*\.env\b(?!\.sample|\.example)',
                r'mv\s+.*\.env\b(?!\.sample|\.example)'
            ]
            return any(re.search(pattern, command) for pattern in env_patterns)
        
        return False


class HookLogger:
    """Handles logging with reduced verbosity."""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.log_path = self.log_dir / "pre_tool_use.json"
    
    def log_tool_usage(self, data: Dict[str, Any]) -> None:
        """Log tool usage data with error handling."""
        try:
            log_data = []
            if self.log_path.exists():
                try:
                    with open(self.log_path, 'r') as f:
                        log_data = json.load(f)
                except (json.JSONDecodeError, IOError):
                    log_data = []
            
            log_data.append(data)
            
            # Keep only last 1000 entries to prevent unbounded growth
            if len(log_data) > 1000:
                log_data = log_data[-1000:]
            
            with open(self.log_path, 'w') as f:
                json.dump(log_data, f, indent=2)
                
        except Exception:
            # Silently fail logging to not disrupt development
            pass


def main():
    """Main hook execution with balanced security approach."""
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            sys.exit(0)
        
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            sys.exit(0)
        
        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})
        
        # Initialize security checker with optional config
        config_path = os.path.join(".claude", "security_config.json")
        security = BalancedSecurityChecker(config_path if os.path.exists(config_path) else None)
        
        # Check .env file access
        should_block, message = security.check_env_file_access(tool_name, tool_input)
        if should_block:
            print(message, file=sys.stderr)
            sys.exit(2)
        
        # Check dangerous rm commands
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            should_block, message = security.check_rm_command(command)
            if should_block:
                print(message, file=sys.stderr)
                sys.exit(2)
        
        # Log tool usage (optional)
        logger = HookLogger()
        logger.log_tool_usage(data)
        
        sys.exit(0)
        
    except Exception:
        # Don't block execution for unexpected errors
        sys.exit(0)


if __name__ == "__main__":
    main()