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

- **PreCompact**: Executes commands before compacting.
- **PreToolUse** and **PostToolUse**: Logs tool usage events.
- **SessionStart** and **Stop**: Plays sounds and logs session events.
- **SubagentStop**: Handles sub-agent termination.
- **UserPromptSubmit**: Logs user prompt submissions.

### Commands

A set of commands is available for specific tasks:

- **Memory Bank Context Optimization**: Reduces token usage in documentation.
- **Claude Code Usage Analysis**: Summarizes usage costs and statistics.
- **UI Healing**: Evaluates and improves user interfaces.
- **Project Analysis**: Provides insights into project structure and organization.

## Project Structure

- `.claude/agents/`: Contains sub-agent configurations.
- `.claude/commands/`: Includes command definitions.
- `.claude/hooks/`: Scripts for hook events.
- `.claude/settings.local.json`: Configuration file for permissions and hooks.

## Getting Started

1. Clone the repository.
2. Review the `.claude/settings.local.json` file to customize permissions and hooks.
3. Explore the `.claude/agents/` directory to understand sub-agent capabilities.
4. Use the commands in `.claude/commands/` to optimize workflows and analyze the project.

## Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or support, please contact the repository owner or open an issue on GitHub.
