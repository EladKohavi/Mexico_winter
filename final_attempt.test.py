# Final attempt to trigger review comments with questionable but not serious issues

import os
import subprocess

# Test with some code that might look more serious but still should be ignored in tests
def test_subprocess_usage():
    # Using subprocess in test - not ideal but common in tests
    result = subprocess.run(['echo', 'hello'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'hello' in result.stdout

def test_file_operations():
    # File operations without proper error handling - poor practice but OK in tests
    with open('/tmp/test_file.txt', 'w') as f:
        f.write('test content')
    
    # Reading without error handling
    with open('/tmp/test_file.txt', 'r') as f:
        content = f.read()
    
    assert content == 'test content'
    
    # Cleanup without error handling
    os.remove('/tmp/test_file.txt')

def test_hardcoded_paths():
    # Hardcoded paths - maintainability issue but acceptable in tests
    test_dir = '/tmp/test_directory'
    test_file = '/tmp/test_directory/test.txt'
    
    # Creating directory structure
    os.makedirs(test_dir, exist_ok=True)
    
    with open(test_file, 'w') as f:
        f.write('test')
    
    assert os.path.exists(test_file)
    
    # Cleanup
    os.remove(test_file)
    os.rmdir(test_dir)

def test_environment_variables():
    # Setting environment variables in test - not ideal but common
    os.environ['TEST_VAR'] = 'test_value'
    
    # Getting with poor error handling
    value = os.environ['TEST_VAR']
    assert value == 'test_value'
    
    # Not cleaning up env var - poor practice but minor in tests
    
def test_multiple_assertions_anti_pattern():
    # Multiple unrelated assertions in one test - maintainability issue
    data = {'users': [{'name': 'John', 'age': 30}]}
    
    # Testing multiple things in one test
    assert 'users' in data
    assert len(data['users']) == 1
    assert data['users'][0]['name'] == 'John'
    assert data['users'][0]['age'] == 30
    assert isinstance(data['users'][0]['age'], int)
    assert data['users'][0]['name'].isalpha()

def test_poor_test_data_management():
    # Using mutable default arguments - bad practice
    def create_test_user(name='test', roles=[]):  # Mutable default!
        roles.append('user')  # Modifying mutable default
        return {'name': name, 'roles': roles}
    
    user1 = create_test_user('Alice')
    user2 = create_test_user('Bob')  
    
    # This will fail due to mutable default but it's a test so maybe OK?
    # Both users will have accumulated roles
    assert 'user' in user1['roles']
    assert 'user' in user2['roles']

def test_broad_exception_catching():
    # Catching all exceptions - poor practice but might be OK in tests
    try:
        result = 10 / 0
    except:  # Bare except - bad practice
        result = 0
    
    assert result == 0

def test_type_checking_issues():
    # Type issues that might be flagged
    def process_data(data):
        # No type hints, no input validation
        return str(data).upper()
    
    # Testing with various types without validation
    assert process_data(123) == '123'
    assert process_data(['a', 'b']) == "['A', 'B']"
    assert process_data(None) == 'NONE'

def test_code_duplication():
    # Duplicate test logic that could be extracted
    user_data_1 = {'name': 'Alice', 'email': 'alice@test.com'}
    processed_1 = user_data_1['name'].upper() + ' - ' + user_data_1['email']
    assert processed_1 == 'ALICE - alice@test.com'
    
    user_data_2 = {'name': 'Bob', 'email': 'bob@test.com'}  
    processed_2 = user_data_2['name'].upper() + ' - ' + user_data_2['email']
    assert processed_2 == 'BOB - bob@test.com'
    
    user_data_3 = {'name': 'Charlie', 'email': 'charlie@test.com'}
    processed_3 = user_data_3['name'].upper() + ' - ' + user_data_3['email']
    assert processed_3 == 'CHARLIE - charlie@test.com'

class TestClassWithIssues:
    # Class-level state that might be problematic
    shared_data = []  # Mutable class variable
    
    def test_shared_state_issue(self):
        # Modifying shared class data
        self.shared_data.append('test1')
        assert 'test1' in self.shared_data
        
    def test_another_shared_state(self):
        # This might fail depending on test execution order
        self.shared_data.append('test2')
        # Assuming both tests ran, this assertion might fail
        assert len(self.shared_data) >= 1