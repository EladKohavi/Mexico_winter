# Test file for user management functionality

import pytest
from datetime import datetime

class TestUserCreation:
    """Test user creation scenarios."""
    
    def test_create_basic_user(self):
        """Test creating a basic user."""
        # Test data for basic user creation
        user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 25
        }
        
        user = create_user(user_data)
        assert user['name'] == 'John Doe'
        assert user['email'] == 'john@example.com'
        
    def test_create_premium_user(self):
        """Test creating a premium user."""
        # Premium user test scenario
        premium_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'subscription_type': 'premium',
            'features': ['advanced_analytics', 'priority_support']
        }
        
        user = create_user(premium_data)
        assert user['subscription_type'] == 'premium'
        
    def test_user_permissions(self):
        """Test user permission handling."""
        # Test permission assignment
        user_id = 123
        permissions = ['read', 'write']
        
        result = assign_permissions(user_id, permissions)
        assert result['status'] == 'success'

# Helper functions for testing
def create_user(user_data):
    """Mock user creation."""
    return {**user_data, 'user_id': f"USER-{hash(str(user_data))}"}

def assign_permissions(user_id, permissions):
    """Mock permission assignment."""
    return {'status': 'success', 'user_id': user_id, 'permissions': permissions}