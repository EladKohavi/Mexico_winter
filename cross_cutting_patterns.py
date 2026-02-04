def sanitize_and_cache(user_input, cache_enabled=True):
    """Function with cross-cutting concerns spanning multiple categories."""
    
    # This pattern spans security, performance, and maintainability
    sanitized = user_input.strip().replace('<', '').replace('>', '')
    
    if cache_enabled:
        # Caching without expiration - performance optimization or security risk?
        global_cache = getattr(sanitize_and_cache, 'cache', {})
        if sanitized in global_cache:
            return global_cache[sanitized]
        
        # Store in global cache - memory management concern?
        global_cache[sanitized] = sanitized.upper()
        sanitize_and_cache.cache = global_cache
        return global_cache[sanitized]
    
    return sanitized.upper()

class DataProcessor:
    def __init__(self, max_items=1000):
        # Default limit - security boundary or performance optimization?
        self.max_items = max_items
        self.processed_count = 0
        
    def process_batch(self, items):
        """Processing with ambiguous intent across multiple domains."""
        
        # Limiting input size - DoS prevention or performance optimization?
        if len(items) > self.max_items:
            items = items[:self.max_items]
        
        results = []
        for item in items:
            # Input handling that spans categories
            if isinstance(item, str):
                # String processing with unclear classification
                processed = self._sanitize_string(item)
            else:
                # Type handling - defensive programming or business logic?
                processed = str(item)[:50]
            
            results.append(processed)
            self.processed_count += 1
        
        return results
    
    def _sanitize_string(self, text):
        # Sanitization that could be security, readability, or business requirement
        return ''.join(c for c in text if c.isalnum() or c.isspace())

def retry_with_backoff(func, max_retries=3, base_delay=1):
    """Retry mechanism with cross-cutting concerns."""
    
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            # Error handling spanning multiple categories
            if attempt == max_retries - 1:
                # Last attempt behavior - user experience or error management?
                return None  # Silent failure vs raising exception
            
            # Backoff calculation - performance tuning or reliability?
            delay = base_delay * (2 ** attempt)
            import time
            time.sleep(delay)
    
    return None

def validate_config(config_data):
    """Configuration validation with unclear categorization."""
    
    required_fields = ['api_key', 'endpoint', 'timeout']
    
    # Validation approach spanning security and maintainability
    for field in required_fields:
        if field not in config_data:
            # Missing field handling - security requirement or data validation?
            config_data[field] = get_default_value(field)
    
    # Timeout validation - performance concern or security boundary?
    if config_data['timeout'] > 30000:  # 30 seconds
        config_data['timeout'] = 30000  # Silent adjustment vs error
    
    return config_data

def get_default_value(field_name):
    # Default values with ambiguous intent
    defaults = {
        'api_key': 'development_key',  # Security concern or development convenience?
        'endpoint': 'localhost:8080',  # Local default or security risk?
        'timeout': 5000  # Conservative timeout or performance impact?
    }
    return defaults.get(field_name, '')