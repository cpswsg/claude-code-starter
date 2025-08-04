#!/usr/bin/env python3
"""
Hook event logging script for Claude Code Template
Logs all hook events to JSON files for later analysis.
"""

import json
import sys
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional


class HookEventLogger:
    """Handles logging of hook events with improved JSON structure."""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
    
    def get_timestamp(self) -> str:
        """Get current UTC timestamp in ISO format."""
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    def extract_event_info(self, hook_input: Dict[str, Any]) -> Dict[str, str]:
        """Extract event information from hook input."""
        return {
            "event_type": hook_input.get("hook_event_name") or hook_input.get("event", "unknown"),
            "tool_name": hook_input.get("tool_name") or hook_input.get("tool", {}).get("name", "unknown"),
            "session_id": hook_input.get("session_id", "unknown"),
            "cwd": hook_input.get("cwd", "unknown")
        }
    
    def create_log_entry(self, hook_input: Dict[str, Any]) -> Dict[str, Any]:
        """Create structured log entry."""
        timestamp = self.get_timestamp()
        event_info = self.extract_event_info(hook_input)
        
        # Extract tool arguments safely
        tool_args = {}
        if "tool_input" in hook_input:
            tool_args = hook_input["tool_input"]
        elif "tool" in hook_input and "arguments" in hook_input["tool"]:
            tool_args = hook_input["tool"]["arguments"]
        
        return {
            "timestamp": timestamp,
            "event_type": event_info["event_type"],
            "tool_name": event_info["tool_name"],
            "session_id": event_info["session_id"],
            "cwd": event_info["cwd"],
            "tool_arguments": tool_args,
            "full_input": hook_input
        }
    
    def write_log_entry(self, log_entry: Dict[str, Any]) -> None:
        """Write log entry to multiple log files."""
        try:
            # Convert to single-line JSON for JSONL format
            json_line = json.dumps(log_entry, separators=(',', ':'))
            
            # Log to daily file
            date = datetime.now().strftime("%Y-%m-%d")
            daily_file = self.log_dir / f"hooks-{date}.jsonl"
            
            # Log to all hooks file
            all_hooks_file = self.log_dir / "all-hooks.jsonl"
            
            # Log to event-specific file
            event_type = log_entry["event_type"].lower().replace(" ", "")
            event_file = self.log_dir / f"{event_type}-events.jsonl"
            
            # Write to all log files
            for log_file in [daily_file, all_hooks_file, event_file]:
                with open(log_file, 'a') as f:
                    f.write(json_line + '\n')
            
            # Output success message to stderr
            tool_name = log_entry["tool_name"]
            event_type = log_entry["event_type"]
            timestamp = log_entry["timestamp"]
            
            if tool_name != "unknown":
                print(f"Logged {event_type} event for tool {tool_name} at {timestamp}", file=sys.stderr)
            else:
                print(f"Logged {event_type} event at {timestamp}", file=sys.stderr)
                
        except Exception as e:
            print(f"Error writing log entry: {e}", file=sys.stderr)
    
    def log_event(self, hook_input: Dict[str, Any]) -> None:
        """Main logging function."""
        log_entry = self.create_log_entry(hook_input)
        self.write_log_entry(log_entry)


def main():
    """Main hook execution function."""
    try:
        # Read hook input from stdin
        input_data = sys.stdin.read().strip()
        if not input_data:
            sys.exit(0)
        
        # Parse JSON input
        try:
            hook_input = json.loads(input_data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON input: {e}", file=sys.stderr)
            sys.exit(0)  # Don't fail the hook for JSON errors
        
        # Initialize logger and log the event
        logger = HookEventLogger()
        logger.log_event(hook_input)
        
        sys.exit(0)
        
    except Exception as e:
        print(f"Hook execution error: {e}", file=sys.stderr)
        sys.exit(0)  # Don't fail the hook for unexpected errors


if __name__ == "__main__":
    main()