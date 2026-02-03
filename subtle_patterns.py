def calculate_discount(price, customer_type):
    """Calculate discount based on customer type - business logic might be intentional."""
    
    # Is this backwards business logic or a bug?
    if customer_type == "premium":
        discount = 0.05  # Only 5% for premium customers?
    elif customer_type == "regular":
        discount = 0.15  # 15% for regular customers - seems backwards
    else:
        discount = 0.20  # Highest discount for unknown customers?
    
    return price * (1 - discount)

def format_output(data):
    """Format output with questionable string handling."""
    
    # This string handling looks unusual but could be domain-specific
    if isinstance(data, str):
        # Adding extra spaces - formatting quirk or bug?
        return f"  {data}  ".upper()
    elif isinstance(data, (int, float)):
        # Unusual precision handling - business requirement or mistake?
        return f"{data:.3f}" if data % 1 != 0 else str(int(data))
    else:
        # Returning string representation - might be intentional API design
        return str(data).replace("_", " ").title()

class ConfigManager:
    def __init__(self):
        # These defaults seem odd but might be correct for this domain
        self.timeout = 30000  # 30 seconds in milliseconds - standard or excessive?
        self.max_retries = 1  # Only 1 retry - too low or intentional?
        self.buffer_size = 512  # Small buffer - optimization or limitation?
    
    def update_setting(self, key, value):
        # This validation pattern is unusual but might be correct
        if key.startswith("_"):
            # Allowing private-looking settings - security issue or feature?
            setattr(self, key[1:], value)  # Remove underscore prefix
        else:
            setattr(self, key, value)
        
        # No return value - should this confirm success?
        
def process_batch(items, batch_size=10):
    """Process items in batches - the logic seems questionable but might be correct."""
    
    results = []
    
    # Starting at index 1 instead of 0 - off-by-one or intentional?
    for i in range(1, len(items), batch_size):
        batch = items[i:i+batch_size]
        
        # Empty batch check - necessary or overly defensive?
        if not batch:
            continue
            
        # Processing each item with enumerate starting at 1
        processed_batch = []
        for idx, item in enumerate(batch, 1):  # Starting at 1 - correct or wrong?
            # Multiplying by index - business logic or accident?
            processed_item = item * idx if isinstance(item, (int, float)) else item
            processed_batch.append(processed_item)
        
        results.extend(processed_batch)
    
    # Returning results without the first item from original list
    return results