#!/usr/bin/env python3
"""
PostToolUse hook for automatic documentation updates.
Triggers documentation generation/updates when code files are modified.
"""

import sys
import json
import os
import subprocess
from pathlib import Path

def log_message(message):
    """Log messages to stderr for debugging"""
    print(f"[DOC-HOOK] {message}", file=sys.stderr)

def is_code_file(file_path):
    """Check if the file is a code file that should trigger doc updates"""
    code_extensions = {
        '.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.cpp', '.c', '.h',
        '.cs', '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.scala',
        '.sh', '.sql', '.yml', '.yaml', '.json'
    }
    return Path(file_path).suffix.lower() in code_extensions

def get_function_signatures(file_path):
    """Extract function signatures from Python files for documentation"""
    if not file_path.endswith('.py'):
        return []
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        import ast
        tree = ast.parse(content)
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get function signature
                args = [arg.arg for arg in node.args.args]
                sig = f"def {node.name}({', '.join(args)})"
                
                # Get docstring if exists
                docstring = ""
                if (node.body and isinstance(node.body[0], ast.Expr) 
                    and isinstance(node.body[0].value, ast.Constant)):
                    docstring = node.body[0].value.value
                
                functions.append({
                    'name': node.name,
                    'signature': sig,
                    'docstring': docstring,
                    'line': node.lineno
                })
        
        return functions
    except Exception as e:
        log_message(f"Error parsing {file_path}: {e}")
        return []

def update_api_docs(changed_files):
    """Update API documentation based on changed files"""
    docs_dir = Path("docs")
    api_doc = docs_dir / "API.md"
    
    # Create docs directory if it doesn't exist
    docs_dir.mkdir(exist_ok=True)
    
    # Collect all Python functions from changed files
    all_functions = []
    for file_path in changed_files:
        if file_path.endswith('.py'):
            functions = get_function_signatures(file_path)
            if functions:
                all_functions.append({
                    'file': file_path,
                    'functions': functions
                })
    
    if not all_functions:
        return
    
    # Generate or update API documentation
    doc_content = "# API Documentation\n\n"
    doc_content += "_Auto-generated from code changes_\n\n"
    
    for file_info in all_functions:
        doc_content += f"## {file_info['file']}\n\n"
        for func in file_info['functions']:
            doc_content += f"### `{func['signature']}`\n\n"
            if func['docstring']:
                doc_content += f"{func['docstring']}\n\n"
            else:
                doc_content += "_No documentation available_\n\n"
            doc_content += f"**Location:** Line {func['line']}\n\n"
    
    # Write the documentation
    with open(api_doc, 'w') as f:
        f.write(doc_content)
    
    log_message(f"Updated API documentation: {api_doc}")

def update_changelog(changed_files):
    """Update CHANGELOG.md with recent changes"""
    changelog = Path("CHANGELOG.md")
    
    # Read existing changelog or create new one
    if changelog.exists():
        with open(changelog, 'r') as f:
            existing_content = f.read()
    else:
        existing_content = "# Changelog\n\n"
    
    # Get current timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create new entry
    new_entry = f"## {timestamp}\n\n"
    new_entry += "**Modified files:**\n"
    for file_path in changed_files:
        new_entry += f"- `{file_path}`\n"
    new_entry += "\n"
    
    # Insert new entry after header
    lines = existing_content.split('\n')
    if len(lines) > 2:
        lines.insert(2, new_entry)
    else:
        lines.append(new_entry)
    
    # Write updated changelog
    with open(changelog, 'w') as f:
        f.write('\n'.join(lines))
    
    log_message(f"Updated changelog: {changelog}")

def main():
    try:
        # Read the hook event data
        hook_data = json.loads(sys.stdin.read())
        
        tool_name = hook_data.get('tool_name', '')
        tool_params = hook_data.get('tool_params', {})
        
        # Only process file write operations
        if tool_name not in ['Write', 'Edit', 'MultiEdit']:
            return
        
        # Extract file paths from different tool types
        changed_files = []
        
        if tool_name == 'Write':
            file_path = tool_params.get('file_path', '')
            if file_path and is_code_file(file_path):
                changed_files.append(file_path)
        
        elif tool_name == 'Edit':
            file_path = tool_params.get('file_path', '')
            if file_path and is_code_file(file_path):
                changed_files.append(file_path)
        
        elif tool_name == 'MultiEdit':
            file_path = tool_params.get('file_path', '')
            if file_path and is_code_file(file_path):
                changed_files.append(file_path)
        
        if not changed_files:
            return
        
        log_message(f"Detected code changes in: {changed_files}")
        
        # Update documentation
        update_api_docs(changed_files)
        update_changelog(changed_files)
        
        # You could also trigger other documentation tools here:
        # - Generate README sections
        # - Update TypeScript declaration files
        # - Generate OpenAPI specs
        # - Update component documentation
        
        log_message("Documentation update completed")
        
    except Exception as e:
        log_message(f"Error in documentation hook: {e}")
        # Don't fail the tool operation if doc update fails
        pass

if __name__ == "__main__":
    main()