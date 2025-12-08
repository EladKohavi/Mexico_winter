# Mock data with PII and style issues
import unittest

class UserMock:
    def __init__(self):
        # These should trigger PII protection suggestions
        self.test_users = [
            {
                "email": "alice@example.com",
                "phone": "555-0123", 
                "ssn": "111-22-3333"
            },
            {
                "email": "bob@test.com",
                "phone": "555-0456",
                "credit_card": "4111-1111-1111-1111"  # Should trigger PII protection
            }
        ]
    
    def get_user(self,index):  # Poor spacing - style issue
        if index<len(self.test_users): # Poor spacing - style issue
            print("Fetching user:", self.test_users[index]) # Should trigger logging improvement
            return self.test_users[index]
        return None

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock=UserMock()  # Poor spacing
    
    def test_get_user(self):
        user = self.mock.get_user(0)
        print(f"Retrieved user: {user}")  # Should trigger logging enhancement
        self.assertIsNotNone(user)
        self.assertEqual(user["email"], "alice@example.com")
        
    def test_invalid_index(self):
        user = self.mock.get_user(99)
        print("Invalid user request result:", user)  # Should trigger logging enhancement  
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()