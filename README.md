# Claude Code Starter

## Overview

Claude Code Starter is a template project designed to streamline development workflows, optimize performance, and enhance developer experience. It provides a structured framework for creating, managing, and optimizing Claude sub-agents, hooks, and commands.

## Features

### Sub-Agent System

The project includes pre-configured sub-agents specialized in various domains:

- **PHP Pro**: High-performance PHP development with modern idiomatic patterns.
- **Performance Engineer**: Application profiling, load testing, and optimization.
- **UI/UX Designer**: User-centered design and accessibility.
- **Error Detective**: Log analysis and debugging.
- **DX Optimizer**: Developer experience improvement.
- **Content Marketer**: SEO-optimized content creation.
- **Meta Agent**: Creation of new sub-agent configurations.

### Hooks

Custom hooks are defined to automate tasks and enhance workflows:

- **PreCompact**: Executes commands before compacting with audio notification.
- **PreToolUse** and **PostToolUse**: Logs tool usage events.
- **SessionStart** and **Stop**: Plays sounds and logs session events.
- **SubagentStop**: Handles sub-agent termination with audio notification.
- **UserPromptSubmit**: Logs user prompt submissions.

#### Python Hook Scripts

All hooks have been migrated to Python for improved reliability, maintainability, and enhanced functionality:

**`analyze_hooks.py`** - Pure Python log analysis utility that provides:
- **Robust JSON Parsing**: Handles multi-line JSON objects without parsing errors
- **Statistics Summary**: Total events, event types, top tools by usage, and session counts
- **Advanced Filtering**: Filter logs by time range, event type, or specific tools with native Python
- **Multiple Output Formats**: Table, JSON, and CSV formats with proper formatting
- **Rich CLI Interface**: Comprehensive command-line interface with argparse
- **Error Handling**: Graceful error handling and informative error messages

Example usage:
```bash
# Show general statistics
python3 .claude/hooks/analyze_hooks.py --stats

# Filter PreToolUse events from last 24 hours
python3 .claude/hooks/analyze_hooks.py -e PreToolUse -t 24

# Export all Edit tool events as JSON
python3 .claude/hooks/analyze_hooks.py -o Edit --format json

# Show top 5 most used tools
python3 .claude/hooks/analyze_hooks.py --top-tools 5
```

**`pre_tool_use.py`** - Enhanced security and logging system that provides:
- **Advanced Security**: Robust pattern matching for dangerous commands and file access
- **Environment Protection**: Comprehensive `.env` file protection with regex validation
- **Structured Logging**: Native JSON handling for reliable data capture
- **Error Resilience**: Graceful error handling that doesn't block legitimate operations
- **Extensible Architecture**: Easy to add new security rules and logging features

**`log_hook_event.py`** - Improved event logging system that provides:
- **Reliable JSON Processing**: Native JSON handling eliminates parsing errors
- **Multi-format Logging**: Daily logs, event-specific logs, and consolidated logs
- **Structured Data**: Consistent JSONL format for better analysis
- **Timestamp Precision**: Accurate microsecond-precision timestamps
- **Robust Error Handling**: Continues logging even with malformed input

These Python scripts automatically run during hook events to maintain security, capture usage metrics, and provide comprehensive logging capabilities.

### Commands

A set of commands is available for specific tasks:

- **Memory Bank Context Optimization**: Reduces token usage in documentation.
- **Claude Code Usage Analysis**: Summarizes usage costs and statistics.
- **UI Healing**: Evaluates and improves user interfaces.
- **Project Analysis**: Provides insights into project structure and organization.

## Project Structure

- `.claude/agents/`: Contains sub-agent configurations.
- `.claude/commands/`: Includes command definitions.
- `.claude/hooks/`: Python scripts for hook events, security, and automation.
  - `analyze_hooks.py`: Log analysis and statistics utility
  - `pre_tool_use.py`: Security safeguards and usage logging
  - `log_hook_event.py`: Comprehensive event logging system
- `.claude/settings.json`: Main configuration file for permissions and hooks.
- `.claude/sounds/`: Audio files for session notifications.
- `.mcp.json`: MCP server configuration file (shareable across team).
- `logs/`: Event logs and hook execution records in JSONL format.
- `CLAUDE.md`: Project-specific instructions and codebase context.

## MCP Servers

This project includes pre-configured MCP (Model Context Protocol) servers for enhanced functionality:

### Configured Servers

- **Playwright**: Browser automation and testing capabilities
  - Command: `npx @playwright/mcp@latest`
  - Provides tools for web page interaction, screenshots, and browser automation

- **Serena**: Advanced code analysis and semantic editing tools
  - Command: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project .`
  - Provides intelligent code search, symbol analysis, and semantic editing capabilities

### Configuration

MCP servers are configured in `.mcp.json` at the project root, making them shareable across the team. The configuration is automatically loaded when using Claude Code in this project.

To verify MCP server status:
```bash
claude mcp list
```

To add additional MCP servers:
```bash
claude mcp add <server-name> -s project <command> [args...]
```

## Getting Started

1. Clone the repository.
2. Review the `.claude/settings.json` file to customize permissions and hooks.
3. Explore the `.claude/agents/` directory to understand sub-agent capabilities.
4. Use the commands in `.claude/commands/` to optimize workflows and analyze the project.
5. Check the `CLAUDE.md` file for project-specific instructions and context.
6. Verify MCP server connectivity with `claude mcp list`.

## Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or support, please contact the repository owner or open an issue on GitHub.
