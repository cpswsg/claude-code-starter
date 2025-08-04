#!/usr/bin/env python3
"""
Hook log analysis utility for Claude Code Template
Provides comprehensive analysis of hook execution patterns and usage statistics.
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict, Counter
import csv
import io


class HookLogAnalyzer:
    """Analyzes Claude Code hook logs with filtering and reporting capabilities."""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.main_log = self.log_dir / "all-hooks.jsonl"
        
        if not self.log_dir.exists():
            raise FileNotFoundError(f"Log directory '{log_dir}' does not exist")
        
        if not self.main_log.exists():
            raise FileNotFoundError(f"Main log file '{self.main_log}' does not exist")
    
    def parse_jsonl(self) -> List[Dict[str, Any]]:
        """Parse JSONL file handling multi-line JSON objects."""
        events = []
        current_lines = []
        in_object = False
        
        try:
            with open(self.main_log, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    if line.startswith('{'):
                        # Process previous object if exists
                        if current_lines:
                            json_str = '\n'.join(current_lines)
                            try:
                                obj = json.loads(json_str)
                                events.append(obj)
                            except json.JSONDecodeError:
                                pass
                        
                        current_lines = [line]
                        in_object = True
                    elif in_object:
                        current_lines.append(line)
                    
                    # Check if current object is complete
                    if in_object and line.endswith('}'):
                        json_str = '\n'.join(current_lines)
                        try:
                            obj = json.loads(json_str)
                            events.append(obj)
                            current_lines = []
                            in_object = False
                        except json.JSONDecodeError:
                            pass
                
                # Handle remaining object
                if current_lines:
                    json_str = '\n'.join(current_lines)
                    try:
                        obj = json.loads(json_str)
                        events.append(obj)
                    except json.JSONDecodeError:
                        pass
                        
        except Exception as e:
            raise RuntimeError(f"Error parsing log file: {e}")
        
        return events
    
    def apply_filters(self, events: List[Dict[str, Any]], 
                     time_hours: Optional[int] = None,
                     event_filter: Optional[str] = None,
                     tool_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """Apply filters to events."""
        filtered_events = events.copy()
        
        # Time filter
        if time_hours:
            cutoff_time = datetime.now() - timedelta(hours=time_hours)
            cutoff_str = cutoff_time.strftime("%Y-%m-%dT%H:%M:%S")
            filtered_events = [
                event for event in filtered_events
                if event.get("timestamp", "") >= cutoff_str
            ]
        
        # Event type filter
        if event_filter:
            filtered_events = [
                event for event in filtered_events
                if event.get("event_type") == event_filter
            ]
        
        # Tool filter
        if tool_filter:
            filtered_events = [
                event for event in filtered_events
                if event.get("tool_name") == tool_filter
            ]
        
        return filtered_events
    
    def show_stats(self):
        """Show comprehensive statistics."""
        events = self.parse_jsonl()
        
        print("=== Hook Log Statistics ===")
        print()
        
        # Total events
        total = len(events)
        print(f"Total events: {total:>8}")
        
        if total == 0:
            print("No events found.")
            return
        
        # Events by type
        print()
        print("Events by type:")
        event_counts = Counter(event.get("event_type", "null") for event in events)
        for event_type, count in event_counts.most_common(10):
            print(f"  {event_type:<20} {count}")
        
        # Tools by usage (excluding unknown)
        print()
        print("Top tools by usage:")
        tool_counts = Counter(
            event.get("tool_name", "null") for event in events
            if event.get("tool_name") not in ["unknown", "null", None]
        )
        for tool_name, count in tool_counts.most_common(10):
            print(f"  {tool_name:<20} {count}")
        
        # Sessions
        print()
        session_ids = set(event.get("session_id") for event in events if event.get("session_id"))
        session_count = len(session_ids)
        print(f"Unique sessions: {session_count:>8}")
        
        # Time range
        print()
        if events:
            timestamps = [event.get("timestamp") for event in events if event.get("timestamp")]
            if timestamps:
                first_event = min(timestamps)
                last_event = max(timestamps)
                print(f"Time range: {first_event} to {last_event}")
            else:
                print("Time range: No valid timestamps found")
        else:
            print("Time range: No valid events found")
    
    def show_top_tools(self, top_n: int = 10):
        """Show top N most used tools."""
        events = self.parse_jsonl()
        
        print(f"=== Top {top_n} Tools ===")
        tool_counts = Counter(
            event.get("tool_name", "null") for event in events
            if event.get("tool_name") not in ["unknown", None]
        )
        
        for i, (tool_name, count) in enumerate(tool_counts.most_common(top_n), 1):
            print(f"{i:>2}. {tool_name:<20} {count}")
    
    def list_events(self):
        """List all event types."""
        events = self.parse_jsonl()
        
        print("=== All Event Types ===")
        event_types = sorted(set(
            event.get("event_type") for event in events
            if event.get("event_type")
        ))
        
        for event_type in event_types:
            print(event_type)
    
    def list_sessions(self):
        """List all sessions."""
        events = self.parse_jsonl()
        
        print("=== All Sessions ===")
        session_ids = sorted(set(
            event.get("session_id") for event in events
            if event.get("session_id") and event.get("session_id") != "unknown"
        ))
        
        for session_id in session_ids:
            print(session_id)
    
    def output_filtered_data(self, output_format: str = "table",
                           time_hours: Optional[int] = None,
                           event_filter: Optional[str] = None,
                           tool_filter: Optional[str] = None):
        """Output filtered data in specified format."""
        events = self.parse_jsonl()
        filtered_events = self.apply_filters(events, time_hours, event_filter, tool_filter)
        
        if output_format == "json":
            for event in filtered_events:
                print(json.dumps(event, separators=(',', ':')))
        
        elif output_format == "csv":
            print("timestamp,event_type,tool_name,session_id")
            for event in filtered_events:
                print(f'"{event.get("timestamp", "")}","{event.get("event_type", "")}","{event.get("tool_name", "")}","{event.get("session_id", "")}"')
        
        else:  # table format
            print("TIMESTAMP                    EVENT_TYPE      TOOL_NAME           SESSION")
            print("---------------------------- --------------- ------------------- --------")
            for event in filtered_events:
                timestamp = event.get("timestamp", "")[:28]
                event_type = event.get("event_type", "")[:15]
                tool_name = event.get("tool_name", "")[:19]
                session_id = event.get("session_id", "")[:8]
                print(f"{timestamp:<28} {event_type:<15} {tool_name:<19} {session_id}")


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Analyze Claude Code hook logs with various filters and output formats.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --stats                           # Show general statistics
  %(prog)s -e PreToolUse -t 24              # PreToolUse events from last 24 hours
  %(prog)s --top-tools 5                    # Top 5 most used tools
  %(prog)s -o Edit --format json            # All Edit tool events as JSON
  %(prog)s --events                         # List all event types
        """
    )
    
    parser.add_argument("-d", "--dir", default="logs", help="Log directory (default: logs)")
    parser.add_argument("-f", "--format", choices=["table", "json", "csv"], default="table",
                       help="Output format (default: table)")
    parser.add_argument("-t", "--time", type=int, help="Filter to last N hours")
    parser.add_argument("-e", "--event", help="Filter by event type")
    parser.add_argument("-o", "--tool", help="Filter by tool name")
    parser.add_argument("--stats", action="store_true", help="Show statistics summary")
    parser.add_argument("--top-tools", type=int, nargs='?', const=10,
                       help="Show top N most used tools (default: 10)")
    parser.add_argument("--events", action="store_true", help="List all event types")
    parser.add_argument("--sessions", action="store_true", help="List all sessions")
    
    args = parser.parse_args()
    
    try:
        analyzer = HookLogAnalyzer(args.dir)
        
        if args.stats:
            analyzer.show_stats()
        elif args.top_tools is not None:
            analyzer.show_top_tools(args.top_tools)
        elif args.events:
            analyzer.list_events()
        elif args.sessions:
            analyzer.list_sessions()
        else:
            analyzer.output_filtered_data(args.format, args.time, args.event, args.tool)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()