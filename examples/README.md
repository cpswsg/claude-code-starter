# Configuration Examples

This directory contains example configurations for different project types. Use these as starting points to customize Claude Code for your specific needs.

## Available Examples

### Currently Available
- **[React TypeScript](./react-typescript/)** - Modern React app with TypeScript, Vite, and testing
- **[FastAPI](./fastapi/)** - Modern Python API with async support and automatic docs

### Coming Soon
Additional examples for popular project types:
- Next.js Full-stack, Vue 3 + Vite, Express API
- Django, Python CLI, Data Science
- React Native, Flutter
- Go API, Rust Web, Microservices
- Electron, Tauri
- Docker, Kubernetes, Terraform

*Contributions welcome! Submit your project configurations as examples.*

## How to Use Examples

### 1. Copy Configuration
```bash
# Copy the example configuration to your project
cp -r examples/react-typescript/.claude ./
cp examples/react-typescript/CLAUDE.md ./
```

### 2. Customize Settings
```bash
# Edit the copied files for your specific needs
$EDITOR CLAUDE.md
$EDITOR .claude/settings.json
```

### 3. Run Setup
```bash
# Use the setup command to finalize configuration
claude setup-project
```

## Example Structure

Each example includes:
- **`.claude/settings.json`** - Tool permissions and hooks for the project type
- **`CLAUDE.md`** - Project-specific context and conventions
- **`README.md`** - Setup instructions and explanations
- **Additional configs** - Framework-specific configurations when needed

## Contributing Examples

Have a configuration that works well for your project type? Contribute it!

1. Create a new directory: `examples/your-project-type/`
2. Include all necessary configuration files
3. Add a comprehensive README.md explaining the setup
4. Submit a pull request

## Template Conventions

All examples follow these conventions:
- **Security First**: Restrictive permissions by default
- **Developer Experience**: Fast feedback loops and good tooling
- **Best Practices**: Follow modern development patterns
- **Documentation**: Clear setup and usage instructions
- **Flexibility**: Easy to customize for specific needs