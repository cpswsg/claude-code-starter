---
description: Analyze current project and recommend optimal technology stack and tooling choices
argument-hint: [focus-area]
allowed-tools: Bash(find:*), Bash(file:*), Bash(ls:*), Bash(cat:*), Read, Glob, Grep
---

# Technology Stack Detection & Analysis

## Context

**Current Project Structure**: !`find . -maxdepth 3 -type f \( -name "*.json" -o -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.go" -o -name "*.java" -o -name "*.rs" -o -name "*.php" -o -name "*.rb" -o -name "*.cs" -o -name "*.swift" -o -name "*.kt" -o -name "package.json" -o -name "requirements.txt" -o -name "Cargo.toml" -o -name "go.mod" -o -name "pom.xml" -o -name "composer.json" -o -name "Gemfile" -o -name "*.csproj" -o -name "Dockerfile" \) | head -20`

**Configuration Files**: !`find . -maxdepth 2 -type f \( -name "package.json" -o -name "requirements.txt" -o -name "pyproject.toml" -o -name "Pipfile" -o -name "Cargo.toml" -o -name "go.mod" -o -name "pom.xml" -o -name "build.gradle" -o -name "composer.json" -o -name "Gemfile" -o -name "*.csproj" -o -name "*.sln" -o -name "yarn.lock" -o -name "package-lock.json" -o -name "poetry.lock" -o -name "Cargo.lock" \)`

**Build and Config Files**: !`find . -maxdepth 2 -type f \( -name "Dockerfile" -o -name "docker-compose.yml" -o -name "Makefile" -o -name "webpack.config.*" -o -name "vite.config.*" -o -name "tsconfig.json" -o -name "babel.config.*" -o -name "eslint*" -o -name "prettier*" -o -name ".gitignore" -o -name "*.toml" -o -name "*.yaml" -o -name "*.yml" \)`

**File Type Distribution**: !`find . -type f | grep -E '\.(js|ts|jsx|tsx|py|go|java|rs|php|rb|cs|swift|kt|html|css|scss|sass|vue|svelte)$' | sed 's/.*\.//' | sort | uniq -c | sort -nr`

## Your Task

Based on the project analysis above, provide a comprehensive technology stack assessment:

### 1. **Current Stack Detection**
Analyze the discovered files and determine:
- **Primary Language(s)**: What programming languages are being used?
- **Framework/Platform**: What frameworks or platforms are in use?
- **Build Tools**: What build systems and task runners are configured?
- **Package Management**: What dependency management systems are present?
- **Development Tools**: What linting, formatting, and quality tools are set up?

### 2. **Project Type Classification**
Classify this project as:
- Web Application (Frontend, Backend, or Full-stack)
- Mobile Application (Native or Cross-platform)
- Desktop Application
- Library/Package
- CLI Tool
- API/Service
- Data Science/ML Project
- Other (specify)

### 3. **Stack Recommendations**
For the detected project type, recommend:
- **Optimal Technology Choices**: Best practices for the current stack
- **Missing Dependencies**: Important packages or tools that should be added
- **Development Environment**: IDE settings, extensions, and configurations
- **Build Optimization**: Improvements to build processes and tooling
- **Testing Strategy**: Appropriate testing frameworks and approaches

### 4. **Modernization Opportunities**
Identify opportunities to:
- Upgrade to newer versions of dependencies
- Adopt modern development practices
- Improve developer experience with better tooling
- Enhance code quality and maintainability
- Optimize for performance and security

### 5. **Claude Code Integration**
Recommend which Claude Code agents and configurations would be most beneficial:
- **Relevant Sub-agents**: Which agents match this project type?
- **Tool Permissions**: What tools should be allowed for this project?
- **Custom Hooks**: What hooks would improve the development workflow?
- **Project-specific Commands**: What custom commands would be useful?

$ARGUMENTS

Focus your analysis on actionable recommendations that will improve the development experience and code quality for this specific project type.