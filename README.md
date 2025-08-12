# Claude Code Starter Kit

## Overview

A comprehensive starter template for setting up Claude Code with optimal configurations, intelligent agents, and productivity-enhancing workflows. This kit provides everything you need to quickly bootstrap Claude Code for any project type.

## 🚀 Quick Start

### Option 1: Use as Template
```bash
# Create a new project from this template
gh repo create my-project --template cswain/claude-code-starter
cd my-project

# Run the interactive setup
claude setup-project
```

### Option 2: Add to Existing Project
```bash
# Clone into your existing project
git clone https://github.com/cswain/claude-code-starter.git temp-starter
cp -r temp-starter/.claude ./
cp temp-starter/.mcp.json ./
cp temp-starter/CLAUDE.md.template ./
rm -rf temp-starter

# Customize for your project
claude setup-project
```

### Option 3: Manual Setup
1. Copy the `.claude/` directory to your project
2. Copy `.mcp.json` for MCP server configuration
3. Copy `CLAUDE.md.template` and customize it as `CLAUDE.md`
4. Copy `.claude/settings.template.json` and customize it as `.claude/settings.json`

## 🎯 What You Get

### Intelligent Agent Library
Pre-configured specialists for any project type:
- **🏗️ Project Initializer**: Intelligent project setup and tech stack configuration
- **⚡ DX Optimizer**: Development workflow optimization and automation
- **🔍 Error Detective**: Advanced debugging and log analysis
- **🎨 UI/UX Designer**: User interface design and accessibility
- **⚙️ Performance Engineer**: Performance monitoring and optimization
- **📝 Content Marketer**: Documentation and content creation
- **🧠 Meta Agent**: Create and customize new agents
- **💻 PHP Pro**: PHP-specific development patterns

### Production-Ready Hook System
Includes both secure and developer-friendly options:
- **🔒 Security Validation**: Two hook options - restrictive (secure) or balanced (developer-friendly)
- **📊 Usage Analytics**: Comprehensive logging and statistics with `analyze_hooks.py`
- **🔔 Audio Notifications**: Optional sound feedback for workflow events (cross-platform customizable)
- **⏰ Session Tracking**: Development time and productivity metrics

> **Note**: The default security hook is quite restrictive. See `HOOK_UPGRADE.md` for a more balanced alternative that warns instead of blocking common operations like `rm -rf node_modules`.

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

## 📋 Configuration Guide

### 1. Essential Setup
```bash
# Copy and customize the main configuration template
cp CLAUDE.md.template CLAUDE.md
# Edit CLAUDE.md with your project-specific information

# Copy and customize settings template
cp .claude/settings.template.json .claude/settings.json
# Edit settings.json for your security and tool preferences
```

### 2. Project-Specific Customization

**For Web Applications:**
```json
// In .claude/settings.json, add:
"allow": [
  "Bash(npm:*)", "Bash(yarn:*)", "Bash(node:*)",
  "Bash(git:*)", "WebFetch(*)"
]
```

**For Python Projects:**
```json
// In .claude/settings.json, add:
"allow": [
  "Bash(python:*)", "Bash(pip:*)", "Bash(pytest:*)",
  "Bash(poetry:*)", "Bash(git:*)"
]
```

**For API Development:**
```json
// In .claude/settings.json, add:
"allow": [
  "Bash(curl:*)", "Bash(docker:*)", "WebFetch(*)",
  "Bash(git:*)"
]
```

### 3. Available Commands

Use these built-in commands to optimize your workflow:
```bash
# Interactive project setup and configuration
claude setup-project [project-type]

# Analyze and recommend optimal tech stack
claude detect-stack [focus-area]

# Optimize development workflow and tooling
claude optimize-workflow [focus-area]

# Generate comprehensive documentation
claude generate-docs [doc-type]

# Analyze project structure and organization
claude analyze-project [focus-area]

# Monitor Claude Code usage and costs
claude ccusage-daily
```

## 🛠️ Customization Examples

### Adding Project-Specific Agents
```bash
# Use the meta-agent to create custom agents
claude meta-agent "Create a database migration agent for my Rails project"
```

### Custom Hook Development
```python
# Add to .claude/hooks/custom_hook.py
def validate_database_migrations():
    # Your custom validation logic
    pass
```

### Environment-Specific Settings
```bash
# Development environment
cp .claude/settings.template.json .claude/settings.local.json
# Customize settings.local.json for your local development needs
```

## 📖 Templates Included

- **`CLAUDE.md.template`**: Comprehensive project context template
- **`.claude/settings.template.json`**: Annotated settings with examples
- **Agent Templates**: Ready-to-use agent configurations
- **Command Templates**: Project setup and optimization commands
- **Hook Templates**: Security and monitoring automation

## 🔧 Advanced Usage

### Multi-Language Projects
```bash
# Configure for polyglot projects
claude setup-project fullstack
# This will detect and configure multiple language support
```

### Team Collaboration
```bash
# Share configurations across team
git add .claude/ .mcp.json
git commit -m "Add Claude Code configuration"
# Team members get consistent Claude Code setup
```

### CI/CD Integration
```yaml
# .github/workflows/claude-analysis.yml
name: Claude Code Analysis
on: [push, pull_request]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Claude Analysis
        run: claude analyze-project ci-cd
```

## 🤝 Contributing

Contributions welcome! This starter kit improves with community input:

- **Agent Templates**: Submit new agent configurations
- **Hook Enhancements**: Improve security and monitoring
- **Documentation**: Better examples and guides
- **Project Templates**: Add support for new frameworks

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/cswain/claude-code-starter/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/cswain/claude-code-starter/discussions)
- 📖 **Documentation**: [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
