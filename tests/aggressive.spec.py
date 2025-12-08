# Python test with aggressive PII and security issues
import unittest
import logging

class AggressiveTestCase(unittest.TestCase):
    def setUp(self):
        # Sensitive test data that should trigger PII warnings
        self.user_data = {
            'email': 'alice.johnson@example.com',
            'password': 'SuperSecret123!',
            'ssn': '987-65-4321',
            'credit_card': '4111-1111-1111-1111',
            'bank_account': '9876543210',
            'api_key': 'sk-abcdef1234567890',
            'oauth_token': 'ya29.abcdefghijklmnopqrstuvwxyz123456',
            'phone': '+1-555-987-6543'
        }
        
        # Database credentials in tests - should trigger security warnings
        self.db_config = {
            'host': 'prod-db.company.com',
            'username': 'admin',
            'password': 'prodPassword123',
            'database': 'production_db'
        }

    def test_user_authentication(self):
        """Test user authentication with sensitive data logging"""
        # Excessive logging of sensitive information
        print(f"Testing authentication for: {self.user_data['email']}")
        print(f"Using password: {self.user_data['password']}")
        print(f"API Key: {self.user_data['api_key']}")
        print(f"OAuth Token: {self.user_data['oauth_token']}")
        
        # Log entire sensitive object
        print("Full user data:", self.user_data)
        
        result = self.authenticate_user()
        self.assertTrue(result)

    def test_payment_processing(self):
        """Test payment with credit card data exposure"""
        # Logging credit card and banking information
        print(f"Processing payment for card: {self.user_data['credit_card']}")
        print(f"Bank account: {self.user_data['bank_account']}")
        print(f"SSN for verification: {self.user_data['ssn']}")
        
        payment_result = self.process_payment()
        self.assertIsNotNone(payment_result)

    def test_database_connection(self):
        """Test with production database credentials"""
        # Logging production database credentials
        print(f"Connecting to: {self.db_config['host']}")
        print(f"Username: {self.db_config['username']}")
        print(f"Password: {self.db_config['password']}")
        print(f"Database: {self.db_config['database']}")
        
        conn_result = self.connect_to_db()
        self.assertTrue(conn_result)

    def authenticate_user(self):
        """Helper method with more sensitive logging"""
        print("Authentication process started")
        print(f"Validating email: {self.user_data['email']}")
        print(f"Password hash input: {self.user_data['password']}")
        return True

    def process_payment(self):
        """Helper method with payment data exposure"""
        print("Payment processing initiated")
        print(f"Card number: {self.user_data['credit_card']}")
        print(f"Account: {self.user_data['bank_account']}")
        return {"transaction_id": "txn_123456", "status": "success"}

    def connect_to_db(self):
        """Helper method with database credential exposure"""
        connection_string = f"postgresql://{self.db_config['username']}:{self.db_config['password']}@{self.db_config['host']}/{self.db_config['database']}"
        print(f"Connection string: {connection_string}")
        return True

if __name__ == '__main__':
    # Configure logging to show sensitive information
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()