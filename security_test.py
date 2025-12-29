# Test file with patterns that might be flagged as more serious issues

import subprocess
import os
import tempfile

def test_command_injection_pattern():
    """Test with subprocess usage that might look concerning."""
    # User input directly in subprocess (looks like command injection)
    user_input = "test_file.txt"
    result = subprocess.run(f"cat {user_input}", shell=True, capture_output=True)
    assert result.returncode == 0

def test_file_permissions():
    """Test with file permission changes."""
    # Creating files with specific permissions
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test content")
        tmp_path = tmp.name
    
    # Changing file permissions (might be flagged)
    os.chmod(tmp_path, 0o777)
    
    # Reading the file
    with open(tmp_path, 'r') as f:
        content = f.read()
    
    assert "test content" in content
    os.unlink(tmp_path)

def test_environment_manipulation():
    """Test with environment variable manipulation."""
    # Setting PATH environment variable (might be concerning)
    original_path = os.environ.get('PATH')
    os.environ['PATH'] = '/bin:/usr/bin'
    
    # Using the modified environment
    result = subprocess.run(['echo', 'hello'], capture_output=True, text=True)
    assert 'hello' in result.stdout
    
    # Not restoring PATH (bad practice)

def test_hardcoded_credentials():
    """Test with hardcoded credentials that might be flagged."""
    # Hardcoded API credentials (security issue)
    api_key = "sk-1234567890abcdef"
    secret_key = "secret_abc123xyz"
    password = "admin123"
    
    # Simulating authentication
    auth_data = {
        'api_key': api_key,
        'secret': secret_key,
        'password': password
    }
    
    # Basic validation
    assert len(auth_data['api_key']) > 0
    assert auth_data['password'] == "admin123"

class TestDangerousPatterns:
    """Test class with potentially dangerous patterns."""
    
    def test_eval_usage(self):
        """Test using eval() which might be flagged."""
        # Using eval (dangerous in production)
        expression = "2 + 2"
        result = eval(expression)
        assert result == 4
        
        # More complex eval usage
        code = "{'key': 'value'}"
        data = eval(code)
        assert data['key'] == 'value'
    
    def test_exec_usage(self):
        """Test using exec() which might be flagged."""
        # Using exec (dangerous)
        code = """
result = 10 * 5
assert result == 50
"""
        exec(code)
    
    def test_file_operations_without_context(self):
        """Test with file operations without proper context managers."""
        # Opening file without with statement (bad practice)
        f = open('/tmp/test_file.txt', 'w')
        f.write('test content')
        f.close()  # Manual close
        
        # Reading without context manager
        f = open('/tmp/test_file.txt', 'r')
        content = f.read()
        f.close()
        
        assert content == 'test content'
        os.unlink('/tmp/test_file.txt')

def test_sql_injection_pattern():
    """Test with SQL-like string formatting that might be flagged."""
    # SQL injection-like pattern
    user_id = "123"
    table_name = "users"
    
    # String formatting that looks like SQL injection
    query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
    
    # Another dangerous pattern
    user_input = "'; DROP TABLE users; --"
    dangerous_query = f"SELECT * FROM users WHERE name = '{user_input}'"
    
    # Simulating query execution
    assert "SELECT" in query
    assert "DROP TABLE" in dangerous_query

def test_pickle_usage():
    """Test with pickle usage that might be flagged."""
    import pickle
    
    # Using pickle (can be dangerous with untrusted data)
    data = {'test': 'value'}
    serialized = pickle.dumps(data)
    
    # Deserializing (potentially dangerous)
    deserialized = pickle.loads(serialized)
    
    assert deserialized['test'] == 'value'

def test_requests_without_verification():
    """Test with HTTP requests without SSL verification."""
    import requests
    
    # HTTP request without SSL verification (security issue)
    try:
        response = requests.get('https://httpbin.org/get', verify=False)
        assert response.status_code == 200
    except:
        # If requests fails, just assert True to avoid test failure
        assert True

def test_weak_random():
    """Test with weak randomization that might be flagged."""
    import random
    
    # Using random (not cryptographically secure)
    token = str(random.randint(100000, 999999))
    session_id = str(random.random())
    
    # Simulating security-related usage
    assert len(token) >= 6
    assert float(session_id) < 1.0