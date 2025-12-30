# Test file for order processing functionality

import pytest
from datetime import datetime

class TestOrderCreation:
    """Test order creation with various scenarios."""
    
    def test_digital_product_order(self):
        """Test digital product order processing."""
        # Test covers digital product workflow
        order_data = {
            'user_id': 123,
            'product_type': 'digital',
            'items': [
                {'product_id': 'ebook-123', 'quantity': 1, 'price': 9.99}
            ],
            'total': 9.99,
            'payment_method': 'credit_card'
        }
        
        # Simulate order creation
        order = create_order(order_data)
        assert order['product_type'] == 'digital'
        assert order['total'] == 9.99
        
    def test_pickup_order(self):
        """Test in-store pickup order processing."""
        pickup_order = {
            'user_id': 456,
            'fulfillment_method': 'store_pickup',
            'store_location': 'Downtown Store',
            'items': [
                {'product_id': 'gadget-456', 'quantity': 2, 'price': 25.00}
            ],
            'total': 50.00
        }
        
        order = create_order(pickup_order)
        assert order['fulfillment_method'] == 'store_pickup'
        
    def test_subscription_order(self):
        """Test subscription order processing."""
        subscription = {
            'user_id': 111,
            'subscription_type': 'trial',
            'plan': 'premium',
            'trial_duration': 30,
            'start_date': datetime.now().isoformat()
        }
        
        result = create_subscription(subscription)
        assert result['subscription_type'] == 'trial'

# Mock functions
def create_order(order_data):
    """Mock order creation function."""
    return {**order_data, 'order_id': f"ORDER-{hash(str(order_data))}"}

def create_subscription(subscription_data):
    """Mock subscription creation function."""
    return {**subscription_data, 'subscription_id': f"SUB-{hash(str(subscription_data))}"}