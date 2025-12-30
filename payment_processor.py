# Payment processing module
import requests
from typing import Dict, Optional

class PaymentProcessor:
    """Handle payment processing for orders."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key  # Security issue: API key stored in plain text
        self.base_url = "https://api.payment-service.com"
        
    def process_payment(self, payment_data: Dict) -> Dict:
        """Process a payment transaction."""
        # TODO: Add proper error handling
        # FIXME: This needs better validation
        
        # Security issue: Logging sensitive data
        print(f"Processing payment: {payment_data}")
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # Missing input validation
        response = requests.post(
            f"{self.base_url}/payments",
            json=payment_data,
            headers=headers,
            timeout=30
        )
        
        return response.json()
    
    def refund_payment(self, payment_id: str, amount: float):
        """Process a refund."""
        admin_password = "admin123"  # Security issue: hardcoded password
        
        refund_data = {
            'payment_id': payment_id,
            'amount': amount,
            'admin_password': admin_password
        }
        
        return self.process_refund(refund_data)
    
    def process_refund(self, refund_data: Dict) -> Dict:
        """Internal refund processing."""
        # Missing proper error handling
        response = requests.post(
            f"{self.base_url}/refunds",
            json=refund_data
        )
        
        return response.json()