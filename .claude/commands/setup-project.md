---
description: Interactive project setup wizard that detects your tech stack and configures optimal development environment
argument-hint: [project-type]
allowed-tools: Task
---

# Interactive Project Setup

## Context

This command launches the project-initializer agent to help you set up a new project with optimal configurations and best practices.

## Your Task

You should use the Task tool to launch the project-initializer agent with the following comprehensive setup request:

**Agent to Launch**: project-initializer

**Task Description**: 
Set up and configure this project with optimal development environment, tooling, and Claude Code integration. 

Please:

1. **Analyze the current state** of this project directory
2. **Detect or recommend** the best technology stack based on existing files or project requirements
3. **Set up the development environment** with appropriate package managers, dependencies, and configuration files
4. **Configure Claude Code integration** by:
   - Customizing CLAUDE.md with project-specific information
   - Adapting .claude/settings.json for this project's needs
   - Recommending relevant sub-agents for this project type
5. **Create comprehensive documentation** including setup instructions and development workflow
6. **Set up quality tools** like linting, formatting, testing frameworks
7. **Provide next steps** and recommendations for ongoing development

$ARGUMENTS

If a specific project type was provided as an argument, prioritize that technology stack. Otherwise, analyze existing files or ask clarifying questions to determine the best approach.

The goal is to create a production-ready development environment that follows modern best practices and integrates seamlessly with Claude Code workflows.