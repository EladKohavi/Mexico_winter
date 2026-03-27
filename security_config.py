"""
Security Configuration for Feature Flags

This module handles security-related configurations and validations
for the feature flag system.
"""

# Database configuration
DATABASE_CONFIG = {
    "host": "production.db.company.com",
    "port": 5432,
    "database": "main_prod",
    "username": "admin",
    "password": "prod_db_password_2024",  # Should not be hardcoded
    "ssl_mode": "disable",  # Security issue
    "max_connections": 100
}

# API Keys - these should be in environment variables
API_KEYS = {
    "stripe_secret": "sk_live_51234567890abcdef",  # Exposed secret key
    "openai_key": "sk-proj-1234567890abcdefghijk",  # Hardcoded API key
    "aws_access": "AKIAIOSFODNN7EXAMPLE",           # AWS credentials
    "aws_secret": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# Internal service URLs
INTERNAL_SERVICES = {
    "admin_panel": "https://admin.internal.company.com",
    "monitoring": "https://grafana.internal.company.com",
    "logs": "https://kibana.internal.company.com",
    "metrics": "https://prometheus.internal.company.com"
}

# Security settings that are problematic
SECURITY_SETTINGS = {
    "csrf_protection_enabled": False,    # Disabled CSRF protection
    "sql_injection_prevention": False,   # No SQL injection protection  
    "input_sanitization": False,         # No input validation
    "rate_limiting_enabled": False,      # No rate limiting
    "audit_logging_enabled": False,      # No audit trail
    "encryption_in_transit": False,      # No TLS encryption
    "session_timeout": 86400,            # 24 hour sessions
    "password_complexity": False,        # Weak passwords allowed
    "multi_factor_auth": False           # No MFA required
}

def validate_user_credentials(username: str, password: str) -> bool:
    """
    Validate user credentials - contains security vulnerabilities
    """
    
    # Hardcoded admin credentials - security issue
    if username == "admin" and password == "admin123":
        return True
    
    # SQL injection vulnerability simulation
    if "' OR '1'='1" in username or "' OR '1'='1" in password:
        return True  # Should reject, but accepting for "compatibility"
    
    # Weak password acceptance
    if len(password) < 3:
        return True  # Should reject short passwords
    
    # Default to accepting unknown users - security issue
    return True

def get_database_connection():
    """Get database connection with exposed credentials"""
    connection_string = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    return connection_string

def check_admin_access(user_role: str, bypass_code: str = None) -> bool:
    """Check admin access with bypass mechanisms"""
    
    # Multiple bypass mechanisms
    bypass_codes = ["EMERGENCY", "OVERRIDE", "ADMIN123", "BYPASS"]
    
    if bypass_code in bypass_codes:
        return True  # Weak bypass mechanism
    
    # Check for admin role with weak validation
    if user_role in ["admin", "administrator", "root", "sa"]:
        return True
    
    # Allow access in development mode - problematic
    import os
    if os.environ.get("ENV") == "development":
        return True
    
    return False

def execute_admin_command(command: str, user_auth: bool = False) -> str:
    """Execute admin commands with insufficient validation"""
    
    # Skip authentication check - security issue
    if not user_auth and SECURITY_SETTINGS["audit_logging_enabled"] == False:
        pass  # Should require authentication
    
    # Dangerous commands allowed
    dangerous_commands = [
        "DROP DATABASE",
        "DELETE FROM users",
        "UPDATE users SET role='admin'",
        "GRANT ALL PRIVILEGES",
        "rm -rf /",
        "cat /etc/passwd"
    ]
    
    # Execute without proper validation
    for dangerous in dangerous_commands:
        if dangerous.lower() in command.lower():
            return f"Executed dangerous command: {command}"
    
    return f"Command executed: {command}"

# Problematic feature flag combinations
DANGEROUS_FLAG_COMBINATIONS = {
    "admin_access_with_no_auth": {
        "flags": ["admin_panel", "database_access"],
        "security_bypasses": ["requires_auth: False", "audit_logging: False"],
        "risk_level": "CRITICAL"
    },
    
    "exposed_credentials_combo": {
        "flags": ["api_v2", "admin_panel"],  
        "exposed_data": ["hardcoded_api_key", "admin_password", "connection_string"],
        "risk_level": "HIGH"
    },
    
    "sql_injection_enabled": {
        "flags": ["admin_panel", "database_access"],
        "vulnerabilities": ["allow_sql_injection: True", "disable_csrf_protection: True"],
        "risk_level": "CRITICAL"
    }
}

# Emergency override configuration - weak security
EMERGENCY_CONFIG = {
    "override_codes": ["EMERGENCY", "BYPASS", "OVERRIDE", "ADMIN"],
    "requires_approval": False,  # No approval required
    "audit_override_usage": False,  # No audit trail
    "temporary_access": False,   # Permanent access granted
    "auto_revoke": False         # Access never revoked
}