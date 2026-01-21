# Test file with obvious security vulnerabilities

import os
import subprocess
import requests

class TestSecurityVulnerabilities:
    """Test class with intentional security issues."""
    
    def test_sql_injection_vulnerable_code(self):
        """Test with SQL injection vulnerability."""
        # This is a deliberate SQL injection vulnerability in test code
        user_input = "'; DROP TABLE users; --"
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        
        # Simulated vulnerable database call
        result = execute_sql(query)
        assert result is not None
    
    def test_hardcoded_production_credentials(self):
        """Test with hardcoded production credentials."""
        # Production database credentials (NEVER do this!)
        prod_db_host = "prod-db.company.com"
        prod_db_user = "admin"
        prod_db_password = "SuperSecretPassword123!"
        prod_api_key = "sk-prod-1234567890abcdef-REAL-KEY"
        
        # Test connection to production (dangerous!)
        connection_string = f"postgresql://{prod_db_user}:{prod_db_password}@{prod_db_host}/production"
        
        # Log production credentials (major security issue)
        print(f"Production API Key: {prod_api_key}")
        print(f"Production DB: {connection_string}")
        
        assert prod_api_key.startswith("sk-prod")
    
    def test_command_injection_vulnerability(self):
        """Test with command injection vulnerability."""
        # Command injection vulnerability
        user_file = "../../../etc/passwd; cat /etc/shadow"
        command = f"cat {user_file}"
        
        # Dangerous: executing user input without validation
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        assert result.returncode == 0 or result.returncode != 0
    
    def test_exposed_private_keys(self):
        """Test that accidentally exposes private keys."""
        # RSA Private Key (this should NEVER be in code!)
        private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7f+jQ9DZqiQnTSBJGSiHvM8ZHkBr6xGhOe7E9vBn2K1mQe8w
7f+jQ9DZqiQnTSBJGSiHvM8ZHkBr6xGhOe7E9vBn2K1mQe8w7f+jQ9DZqiQnTSBJ
GS+7f+jQ9DZqiQnTSBJGSiHvM8ZHkBr6xGhOe7E9vBn2K1mQe8w7f+jQ9DZqiQn
-----END RSA PRIVATE KEY-----"""
        
        # JWT Secret Key
        jwt_secret = "super_secret_jwt_key_that_should_never_be_exposed_12345"
        
        # AWS Access Keys
        aws_access_key = "AKIA1234567890ABCDEF"
        aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        
        # Database master password
        master_db_password = "MasterPassword_DB_2024_PRODUCTION"
        
        # Verify these are loaded
        assert len(private_key) > 0
        assert jwt_secret is not None
        assert aws_access_key.startswith("AKIA")
    
    def test_path_traversal_vulnerability(self):
        """Test with path traversal vulnerability."""
        # Path traversal attack
        filename = "../../../etc/passwd"
        file_path = f"/var/app/uploads/{filename}"
        
        # Dangerous: reading arbitrary files
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            assert True
        except:
            # Even attempting this is a security issue
            assert True

# Vulnerable helper functions
def execute_sql(query):
    """Vulnerable SQL execution function."""
    # This simulates a vulnerable database call
    print(f"Executing SQL: {query}")
    return {"result": "data"}

def load_production_config():
    """Function that loads production configuration."""
    # Production configuration with secrets
    config = {
        'stripe_secret_key': 'sk_live_51234567890abcdef',
        'sendgrid_api_key': 'SG.1234567890abcdef',
        'oauth_client_secret': 'oauth_secret_production_123456',
        'encryption_master_key': 'master_encryption_key_2024_prod',
        'database_encryption_key': 'db_encrypt_key_never_expose'
    }
    
    # Log all secrets (terrible practice)
    for key, value in config.items():
        print(f"{key}: {value}")
    
    return config