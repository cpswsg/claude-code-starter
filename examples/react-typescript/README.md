# React + TypeScript Configuration

This example provides a complete Claude Code configuration for modern React applications with TypeScript.

## What's Included

### 🎯 Optimized Tool Permissions
- **Node.js Tools**: npm, yarn, node commands
- **Git Integration**: Full git workflow support
- **Development Safety**: Prevents dangerous file deletions
- **Selective Write Access**: Only allows writes to source and test files

### 🔧 Smart Hooks
- **Dependency Monitoring**: Alerts after npm installs
- **Security Validation**: Prevents sensitive file access
- **Development Logging**: Tracks usage patterns

### 📋 Project Context
- React 18 + TypeScript best practices
- Modern tooling with Vite
- Testing with Vitest and React Testing Library
- Performance optimization guidelines
- Security and accessibility considerations

## Quick Setup

```bash
# Copy configuration to your React project
cp -r examples/react-typescript/.claude ./
cp examples/react-typescript/CLAUDE.md ./

# Customize settings if needed
$EDITOR .claude/settings.json
$EDITOR CLAUDE.md

# Verify Claude Code integration
claude detect-stack
```

## Key Features

### Development Workflow
- **Fast Development**: Vite dev server with HMR
- **Type Safety**: Strict TypeScript configuration
- **Code Quality**: ESLint + Prettier + pre-commit hooks
- **Testing**: Comprehensive testing setup with coverage

### Claude Code Integration
- **Smart Agents**: UI/UX Designer, Performance Engineer, Error Detective
- **Security**: Protects .env files and prevents dangerous operations
- **Automation**: Automatic dependency auditing and type checking

### Best Practices
- Component-based architecture
- Custom hooks for business logic
- React Query for server state
- TypeScript interfaces for all data

## Recommended Agents

For React TypeScript projects, these agents are particularly useful:

```bash
# UI/UX optimization and accessibility
claude ui-ux-designer

# Performance monitoring and optimization
claude performance-engineer

# Debugging React-specific issues
claude error-detective

# Development workflow optimization
claude dx-optimizer
```

## Customization Options

### Stricter Security
```json
// Remove write permissions for source files
"deny": [
  "Write(**/src/**)",
  "Edit(**/src/**)"
]
```

### Additional Tools
```json
// Add support for additional tools
"allow": [
  "Bash(docker:*)",      // Docker commands
  "Bash(storybook:*)",   // Storybook development
  "WebFetch(domain:*)"   // Unrestricted web access
]
```

### Framework Variations

This configuration works well for:
- **Vite + React**: Default configuration
- **Create React App**: Remove Vite-specific permissions
- **Next.js**: Add server-side rendering considerations
- **Remix**: Add server/client boundary awareness

## Common Commands

```bash
# Project analysis and recommendations
claude detect-stack react

# Optimize development workflow
claude optimize-workflow frontend

# Generate documentation
claude generate-docs

# Analyze project structure
claude analyze-project
```

## Troubleshooting

### Permission Issues
If Claude can't run certain commands, check the `allow` list in `.claude/settings.json`.

### Hook Failures
Ensure Python 3 is available for hook execution:
```bash
python3 --version
# Should show Python 3.x.x
```

### MCP Server Issues
Verify MCP servers are configured:
```bash
claude mcp list
# Should show available servers
```

## Related Examples

- **[FastAPI](../fastapi/)** - Backend API companion

### Coming Soon
- Next.js Full-stack - Server-side rendering
- Express API - Node.js backend
- React Native - Mobile development
- Electron - Desktop applications