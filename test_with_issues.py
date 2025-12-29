# Test file designed to trigger specific review comments about style and maintainability

import pytest
import requests
import json

class TestUserManagement:
    """Test class with various issues that commonly trigger review comments."""
    
    def test_user_creation(self):
        # Magic numbers without explanation
        response = requests.post('http://localhost:8000/users', json={
            'name': 'John Doe',
            'age': 25,
            'role': 'admin'
        })
        
        # Hardcoded status code
        assert response.status_code == 201
        
        # Accessing nested data without validation  
        user_id = response.json()['id']
        assert user_id > 0

    def test_user_retrieval(self):
        # Duplicate URL from above test - code duplication
        base_url = 'http://localhost:8000'
        
        # Create user first (duplicate logic)
        create_response = requests.post(f'{base_url}/users', json={
            'name': 'Jane Smith', 
            'age': 30,
            'role': 'user'
        })
        user_id = create_response.json()['id']
        
        # Get user
        get_response = requests.get(f'{base_url}/users/{user_id}')
        assert get_response.status_code == 200
        
        user_data = get_response.json()
        assert user_data['name'] == 'Jane Smith'

    def test_user_update_with_poor_structure(self):
        # Very long test method that does too many things
        base_url = 'http://localhost:8000'  # Repeated constant
        
        # Create user (repeated logic again)
        user_data = {'name': 'Bob Wilson', 'age': 35, 'role': 'manager'}
        create_resp = requests.post(f'{base_url}/users', json=user_data)
        user_id = create_resp.json()['id']
        
        # Update user
        update_data = {'age': 36}
        update_resp = requests.put(f'{base_url}/users/{user_id}', json=update_data)
        assert update_resp.status_code == 200
        
        # Verify update
        get_resp = requests.get(f'{base_url}/users/{user_id}')
        updated_user = get_resp.json()
        assert updated_user['age'] == 36
        
        # Delete user (adding more responsibilities to this test)
        delete_resp = requests.delete(f'{base_url}/users/{user_id}')
        assert delete_resp.status_code == 204
        
        # Verify deletion
        verify_resp = requests.get(f'{base_url}/users/{user_id}')
        assert verify_resp.status_code == 404


def test_data_processing():
    """Standalone test function with maintainability issues."""
    
    # Complex nested data structure
    test_data = {
        'users': [
            {'id': 1, 'name': 'Alice', 'permissions': ['read', 'write']},
            {'id': 2, 'name': 'Bob', 'permissions': ['read']},
            {'id': 3, 'name': 'Charlie', 'permissions': ['read', 'write', 'admin']}
        ]
    }
    
    # Multiple assertions testing different aspects (could be separate tests)
    assert len(test_data['users']) == 3
    assert test_data['users'][0]['name'] == 'Alice'
    assert 'write' in test_data['users'][0]['permissions']
    assert len(test_data['users'][2]['permissions']) == 3
    
    # Complex processing logic in test
    admin_users = []
    for user in test_data['users']:
        if 'admin' in user['permissions']:
            admin_users.append(user)
    
    assert len(admin_users) == 1
    assert admin_users[0]['name'] == 'Charlie'


def test_with_hardcoded_values():
    """Test with many hardcoded values that could be constants."""
    
    # Multiple hardcoded strings that could be constants
    api_key = 'test-api-key-12345'
    base_url = 'https://api.example.com/v1'
    timeout_seconds = 30
    max_retries = 3
    
    # Simulated API call with hardcoded values
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'User-Agent': 'TestClient/1.0'
    }
    
    # Mock response data with hardcoded structure
    mock_response = {
        'status': 'success',
        'data': {
            'items': [
                {'id': 101, 'name': 'Item 1'},
                {'id': 102, 'name': 'Item 2'}
            ]
        }
    }
    
    # Assertions with magic numbers
    assert mock_response['status'] == 'success'
    assert len(mock_response['data']['items']) == 2
    assert mock_response['data']['items'][0]['id'] == 101


class TestDatabaseOperations:
    """Test class with setup/teardown issues."""
    
    def setup_method(self):
        # Hardcoded database connection string
        self.db_url = 'postgresql://test:password@localhost:5432/testdb'
        self.test_user_id = None
    
    def test_user_crud_operations(self):
        # This test does too many operations (Create, Read, Update, Delete)
        
        # CREATE
        user_data = {
            'username': 'testuser123',
            'email': 'test@example.com',
            'is_active': True
        }
        # Simulate user creation
        self.test_user_id = 12345  # Hardcoded ID
        
        # READ
        # Simulate user retrieval
        retrieved_user = {
            'id': self.test_user_id,
            'username': 'testuser123',
            'email': 'test@example.com',
            'is_active': True
        }
        assert retrieved_user['username'] == 'testuser123'
        
        # UPDATE  
        update_data = {'is_active': False}
        # Simulate update
        updated_user = retrieved_user.copy()
        updated_user.update(update_data)
        assert updated_user['is_active'] == False
        
        # DELETE
        # Simulate deletion
        deletion_result = {'success': True}
        assert deletion_result['success'] == True


def test_complex_validation_logic():
    """Test with complex validation that could be simplified."""
    
    test_cases = [
        {'input': 'valid@email.com', 'expected': True},
        {'input': 'invalid-email', 'expected': False},
        {'input': 'another@valid.email.org', 'expected': True},
        {'input': '', 'expected': False},
        {'input': '@invalid.com', 'expected': False}
    ]
    
    # Manual validation logic instead of using a proper validator
    for case in test_cases:
        email = case['input']
        expected = case['expected']
        
        # Crude email validation (could trigger maintainability comments)
        is_valid = False
        if email and '@' in email:
            parts = email.split('@')
            if len(parts) == 2 and parts[0] and parts[1]:
                if '.' in parts[1]:
                    domain_parts = parts[1].split('.')
                    if len(domain_parts) >= 2 and all(part for part in domain_parts):
                        is_valid = True
        
        assert is_valid == expected, f"Email validation failed for {email}"