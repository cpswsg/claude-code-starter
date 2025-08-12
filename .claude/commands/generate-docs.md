---
description: Generate comprehensive project documentation based on code analysis and best practices
argument-hint: [doc-type]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(find:*), Bash(ls:*)
---

# Comprehensive Documentation Generator

## Context

**Project Files**: !`find . -type f \( -name "*.md" -o -name "*.txt" -o -name "README*" -o -name "CHANGELOG*" -o -name "CONTRIBUTING*" \) | head -10`

**Code Structure**: !`find . -type f \( -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.go" -o -name "*.java" -o -name "*.rs" \) | head -15`

**Configuration Files**: !`find . -maxdepth 2 -type f \( -name "package.json" -o -name "requirements.txt" -o -name "Cargo.toml" -o -name "go.mod" -o -name "pyproject.toml" \)`

## Your Task

Generate comprehensive documentation for this project based on code analysis and modern documentation best practices.

### **Documentation Types Available**

Choose based on the argument provided or create all if no specific type is requested:

#### **1. README.md** (default if no argument)
Create a comprehensive README including:
- **Project Overview**: Clear description of what the project does
- **Features**: Key capabilities and functionality
- **Installation**: Step-by-step setup instructions
- **Usage**: Basic usage examples and code snippets
- **Configuration**: Environment variables and settings
- **Contributing**: How to contribute to the project
- **License**: License information
- **Contact**: Support and contact information

#### **2. API Documentation** (api)
For projects with APIs, create:
- **Endpoint Documentation**: All available endpoints with examples
- **Authentication**: How to authenticate with the API
- **Request/Response Formats**: Data structures and formats
- **Error Handling**: Error codes and response formats
- **Rate Limiting**: Usage limits and best practices
- **SDKs and Examples**: Code examples in multiple languages

#### **3. Contributing Guidelines** (contributing)
Create CONTRIBUTING.md with:
- **Development Setup**: How to set up the development environment
- **Code Standards**: Coding conventions and style guidelines
- **Pull Request Process**: How to submit changes
- **Issue Reporting**: How to report bugs and request features
- **Testing Requirements**: How to write and run tests
- **Release Process**: How releases are managed

#### **4. Architecture Documentation** (architecture)
Create technical architecture documentation:
- **System Overview**: High-level architecture diagrams
- **Component Relationships**: How different parts interact
- **Data Flow**: How data moves through the system
- **Technology Choices**: Why specific technologies were chosen
- **Deployment Architecture**: How the system is deployed
- **Security Considerations**: Security patterns and practices

#### **5. User Guide** (user-guide)
Create end-user documentation:
- **Getting Started**: Quick start guide for new users
- **Feature Walkthroughs**: Detailed feature explanations
- **Tutorials**: Step-by-step tutorials for common tasks
- **Troubleshooting**: Common issues and solutions
- **FAQ**: Frequently asked questions
- **Tips and Best Practices**: Advanced usage tips

#### **6. Developer Guide** (dev-guide)
Create developer-focused documentation:
- **Codebase Overview**: Understanding the code structure
- **Development Workflow**: How to work with the codebase
- **Testing Strategy**: How to write and maintain tests
- **Debugging**: How to debug and troubleshoot issues
- **Performance**: Performance considerations and optimization
- **Security**: Security practices and considerations

### **Implementation Approach**

1. **Analyze Existing Documentation**
   - Read current documentation files to understand what exists
   - Identify gaps and areas for improvement
   - Preserve valuable existing content

2. **Code Analysis**
   - Examine the codebase to understand functionality
   - Extract key features and capabilities
   - Identify main entry points and usage patterns

3. **Generate Documentation**
   - Create well-structured, readable documentation
   - Include practical examples and code snippets
   - Follow markdown best practices for formatting
   - Add appropriate badges and visual elements

4. **Validation**
   - Ensure all links work and examples are accurate
   - Verify setup instructions by following them
   - Check that documentation matches actual code behavior

### **Best Practices**

- **User-Focused**: Write from the user's perspective
- **Practical Examples**: Include real, working code examples
- **Keep Updated**: Include instructions for keeping docs current
- **Visual Elements**: Use diagrams, screenshots when helpful
- **Searchable**: Structure content for easy navigation
- **Accessible**: Use clear language and good formatting
- **Comprehensive**: Cover all important aspects thoroughly
- **Maintainable**: Make it easy to update and extend

$ARGUMENTS

The documentation should be professional, comprehensive, and immediately useful to both new users and experienced developers working with this project.