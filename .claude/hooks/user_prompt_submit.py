#!/usr/bin/env python3
"""
UserPromptSubmit hook for validating and sanitizing user inputs.
Provides security validation, content filtering, and quality control.
"""

import sys
import json
import re
from datetime import datetime
from pathlib import Path

def log_message(message, level="INFO"):
    """Log messages to stderr for debugging"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [VALIDATION-{level}] {message}", file=sys.stderr)

def check_malicious_patterns(prompt):
    """Check for potentially malicious patterns in user input"""
    malicious_patterns = [
        # Command injection attempts
        r';\s*(rm|del|format|shutdown|halt)\s',
        r'\|\s*(rm|del|format|shutdown|halt)\s',
        r'&&\s*(rm|del|format|shutdown|halt)\s',
        
        # File system manipulation
        r'\.\./',  # Directory traversal
        r'\\.\\.\\',  # Windows directory traversal
        r'/etc/passwd',
        r'/etc/shadow',
        r'C:\\Windows\\System32',
        
        # Network/security attempts
        r'curl\s+.*\|\s*sh',
        r'wget\s+.*\|\s*sh',
        r'nc\s+-l',  # Netcat listener
        r'ncat\s+-l',
        
        # SQL injection patterns
        r"(union|select|insert|update|delete|drop)\s+.*from\s+",
        r"'.*or.*'.*=.*'",
        r'".*or.*".*=.*"',
        
        # Script injection
        r'<script[^>]*>',
        r'javascript:',
        r'eval\s*\(',
        r'exec\s*\(',
        
        # Cryptocurrency/mining
        r'(bitcoin|ethereum|mining|crypto).*wallet',
        r'(btc|eth).*address',
        
        # Sensitive data patterns
        r'password\s*[=:]\s*["\']?\w+',
        r'api[_-]?key\s*[=:]\s*["\']?\w+',
        r'secret\s*[=:]\s*["\']?\w+',
        r'token\s*[=:]\s*["\']?\w+',
    ]
    
    violations = []
    for pattern in malicious_patterns:
        matches = re.finditer(pattern, prompt, re.IGNORECASE)
        for match in matches:
            violations.append({
                'pattern': pattern,
                'match': match.group(),
                'position': match.span()
            })
    
    return violations

def check_content_quality(prompt):
    """Check for content quality issues"""
    warnings = []
    
    # Check for extremely long prompts (potential spam)
    if len(prompt) > 10000:
        warnings.append("Extremely long prompt detected (>10k chars)")
    
    # Check for repetitive content
    words = prompt.lower().split()
    if len(words) > 50:
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Find most frequent word
        max_freq = max(word_freq.values())
        if max_freq > len(words) * 0.3:  # More than 30% repetition
            warnings.append(f"High repetition detected ({max_freq} occurrences)")
    
    # Check for potential spam indicators
    spam_indicators = [
        r'(click|visit).*https?://',
        r'buy\s+now',
        r'limited\s+time',
        r'act\s+fast',
        r'urgent\s+response',
        r'\$\d+.*guaranteed',
    ]
    
    for pattern in spam_indicators:
        if re.search(pattern, prompt, re.IGNORECASE):
            warnings.append(f"Potential spam pattern: {pattern}")
    
    return warnings

def check_file_safety(prompt):
    """Check for unsafe file operations"""
    unsafe_patterns = [
        # Dangerous file operations
        r'(write|create|delete|remove).*\.env',
        r'(write|create|delete|remove).*/etc/',
        r'(write|create|delete|remove).*/root/',
        r'(write|create|delete|remove).*\.ssh/',
        r'(write|create|delete|remove).*\.aws/',
        
        # System files
        r'hosts\s+file',
        r'/etc/hosts',
        r'C:\\Windows\\System32\\drivers\\etc\\hosts',
        
        # Configuration files
        r'\.bashrc',
        r'\.zshrc',
        r'\.profile',
        r'config\.json',
        
        # Backup/sensitive extensions
        r'\.(bak|backup|old|orig)$',
        r'\.(key|pem|p12|pfx)$',
    ]
    
    violations = []
    for pattern in unsafe_patterns:
        matches = re.finditer(pattern, prompt, re.IGNORECASE)
        for match in matches:
            violations.append({
                'pattern': pattern,
                'match': match.group(),
                'position': match.span(),
                'type': 'file_safety'
            })
    
    return violations

def sanitize_prompt(prompt):
    """Sanitize potentially dangerous content while preserving intent"""
    # Remove potential script injections
    sanitized = re.sub(r'<script[^>]*>.*?</script>', '[SCRIPT_REMOVED]', prompt, flags=re.IGNORECASE | re.DOTALL)
    
    # Mask potential credentials (but keep structure for legitimate examples)
    sanitized = re.sub(r'(password|api[_-]?key|secret|token)\s*[=:]\s*["\']?(\w+)', r'\1=***MASKED***', sanitized, flags=re.IGNORECASE)
    
    # Mask email addresses in non-code contexts
    if not re.search(r'(code|example|demo|test)', prompt, re.IGNORECASE):
        sanitized = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL_MASKED]', sanitized)
    
    # Mask potential crypto addresses
    sanitized = re.sub(r'\b(1|3)[A-HJ-NP-Z0-9]{25,34}\b', '[BTC_ADDRESS_MASKED]', sanitized)  # Bitcoin
    sanitized = re.sub(r'\b0x[a-fA-F0-9]{40}\b', '[ETH_ADDRESS_MASKED]', sanitized)  # Ethereum
    
    return sanitized

def validate_project_context(prompt):
    """Validate that requests are appropriate for the current project"""
    warnings = []
    
    # Check if user is asking for operations outside project scope
    external_indicators = [
        r'download.*from.*internet',
        r'install.*globally',
        r'modify.*system.*settings',
        r'access.*other.*projects',
        r'send.*email',
        r'post.*to.*social',
    ]
    
    for pattern in external_indicators:
        if re.search(pattern, prompt, re.IGNORECASE):
            warnings.append(f"Request may be outside project scope: {pattern}")
    
    return warnings

def log_validation_result(prompt, violations, warnings, sanitized_prompt):
    """Log validation results for audit purposes"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    validation_log = log_dir / "validation.jsonl"
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "original_length": len(prompt),
        "sanitized_length": len(sanitized_prompt),
        "violations_count": len(violations),
        "warnings_count": len(warnings),
        "violations": violations,
        "warnings": warnings,
        "prompt_hash": hash(prompt),  # For tracking without storing full content
    }
    
    with open(validation_log, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def main():
    try:
        # Read the hook event data
        hook_data = json.loads(sys.stdin.read())
        
        prompt = hook_data.get('prompt', '')
        
        if not prompt:
            return
        
        log_message(f"Validating prompt ({len(prompt)} chars)")
        
        # Run all validation checks
        malicious_violations = check_malicious_patterns(prompt)
        file_safety_violations = check_file_safety(prompt)
        quality_warnings = check_content_quality(prompt)
        context_warnings = validate_project_context(prompt)
        
        all_violations = malicious_violations + file_safety_violations
        all_warnings = quality_warnings + context_warnings
        
        # Sanitize the prompt
        sanitized_prompt = sanitize_prompt(prompt)
        
        # Log results
        log_validation_result(prompt, all_violations, all_warnings, sanitized_prompt)
        
        # Handle violations (block dangerous requests)
        if malicious_violations:
            log_message(f"SECURITY VIOLATION: Found {len(malicious_violations)} malicious patterns", "ERROR")
            for violation in malicious_violations:
                log_message(f"  - Pattern: {violation['pattern']}", "ERROR")
                log_message(f"  - Match: {violation['match']}", "ERROR")
            
            # Create blocking response
            print(json.dumps({
                "block": True,
                "reason": f"Security violation: Found {len(malicious_violations)} potentially malicious patterns",
                "violations": malicious_violations
            }))
            return
        
        # Handle file safety violations
        if file_safety_violations:
            log_message(f"FILE SAFETY WARNING: Found {len(file_safety_violations)} unsafe file operations", "WARN")
            for violation in file_safety_violations:
                log_message(f"  - Pattern: {violation['pattern']}", "WARN")
                log_message(f"  - Match: {violation['match']}", "WARN")
        
        # Handle warnings (log but allow)
        if all_warnings:
            log_message(f"Content warnings: {len(all_warnings)} issues detected", "WARN")
            for warning in all_warnings:
                log_message(f"  - {warning}", "WARN")
        
        # Log sanitization if it occurred
        if sanitized_prompt != prompt:
            log_message("Prompt was sanitized", "INFO")
        
        log_message("Validation completed successfully")
        
    except Exception as e:
        log_message(f"Error in validation hook: {e}", "ERROR")
        # Don't fail the user's request if validation fails
        pass

if __name__ == "__main__":
    main()