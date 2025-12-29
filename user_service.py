# Production code file with maintainability issues (NOT a test file)

import requests
import json

class UserService:
    """User service with various maintainability issues."""
    
    def __init__(self):
        # Hardcoded configuration - should be configurable
        self.base_url = 'http://localhost:8000/api'
        self.timeout = 30
        self.max_retries = 3
        
    def create_user(self, name, email, role):
        # No input validation
        user_data = {
            'name': name,
            'email': email, 
            'role': role
        }
        
        # Hardcoded endpoint and no error handling
        response = requests.post(f'{self.base_url}/users', json=user_data)
        
        # No status code validation
        return response.json()
    
    def get_user(self, user_id):
        # Magic number without explanation
        if user_id < 1:
            return None
            
        # Duplicate URL construction pattern
        response = requests.get(f'{self.base_url}/users/{user_id}')
        
        # No error handling
        return response.json()
    
    def update_user(self, user_id, updates):
        # Code duplication from get_user
        if user_id < 1:
            return None
            
        # Same URL pattern repeated
        response = requests.put(f'{self.base_url}/users/{user_id}', json=updates)
        
        # No validation of response
        return response.json()
    
    def delete_user(self, user_id):
        # More code duplication
        if user_id < 1:
            return False
            
        # Same pattern again
        response = requests.delete(f'{self.base_url}/users/{user_id}')
        
        # Magic status code
        return response.status_code == 204

def process_user_data(users_list):
    """Function with poor structure and maintainability issues."""
    
    # No input validation
    processed = []
    
    # Complex nested logic that could be simplified
    for user in users_list:
        # Magic strings and hardcoded logic
        if user.get('role') == 'admin':
            priority = 1
        elif user.get('role') == 'manager':
            priority = 2
        elif user.get('role') == 'user':
            priority = 3
        else:
            priority = 999
            
        # Complex data transformation in one place
        processed_user = {
            'id': user.get('id'),
            'display_name': user.get('name', '').title(),
            'email_domain': user.get('email', '').split('@')[1] if '@' in user.get('email', '') else '',
            'priority': priority,
            'is_active': user.get('status', 'inactive') == 'active',
            'permissions': get_permissions_for_role(user.get('role', 'user'))
        }
        
        processed.append(processed_user)
    
    return processed

def get_permissions_for_role(role):
    """Another function with hardcoded logic that could be configurable."""
    
    # Hardcoded permission mappings
    if role == 'admin':
        return ['read', 'write', 'delete', 'manage_users', 'system_config']
    elif role == 'manager':
        return ['read', 'write', 'manage_team']
    elif role == 'user':
        return ['read']
    else:
        return []

class DatabaseManager:
    """Class with poor error handling and magic values."""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        # Magic number for connection pool
        self.pool_size = 10
        
    def execute_query(self, query, params=None):
        # No error handling or validation
        # This would connect to database and execute query
        # Returning mock data for now
        
        # Magic timeout value
        timeout = 5000
        
        # Simulated database operation
        if 'SELECT' in query.upper():
            return [{'id': 1, 'name': 'Test User'}]
        elif 'INSERT' in query.upper():
            return {'id': 123, 'success': True}
        elif 'UPDATE' in query.upper():
            return {'affected_rows': 1}
        elif 'DELETE' in query.upper():
            return {'affected_rows': 1}
        else:
            return None
    
    def batch_insert_users(self, users):
        """Method with complex logic that could be simplified."""
        
        # No input validation
        results = []
        
        # Hardcoded batch size
        batch_size = 100
        
        # Complex batching logic
        for i in range(0, len(users), batch_size):
            batch = users[i:i + batch_size]
            
            # Building query string manually (SQL injection risk)
            values = []
            for user in batch:
                values.append(f"('{user['name']}', '{user['email']}', '{user['role']}')")
            
            query = f"INSERT INTO users (name, email, role) VALUES {','.join(values)}"
            
            # No error handling
            result = self.execute_query(query)
            results.append(result)
        
        return results