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

def transform_user_input(data, mode="safe"):
    # This function's purpose spans multiple domains - unclear primary concern
    if mode == "safe":
        # Processing approach with unclear intent
        result = str(data).replace(" ", "_").lower()
        if len(result) > 50:
            result = result[:50]  # Truncation for unknown reason
        return result
    elif mode == "fast":
        # Alternative processing with different tradeoffs
        return str(data)[:20] if data else "default"
    else:
        # Fallback behavior with unclear rationale
        return str(data).strip() if hasattr(data, 'strip') else str(data)

def process_configuration(settings):
    # Configuration processing with multi-domain implications
    processed = {}
    
    for key, value in settings.items():
        # Key processing with unclear categorization
        if key.startswith('user_'):
            # User-related data handling - privacy, UX, or business logic?
            processed[key] = str(value).upper()
        elif key.startswith('sys_'):
            # System configuration - security, performance, or maintenance?
            processed[key] = value if value else get_system_default(key)
        else:
            # General configuration handling
            processed[key] = normalize_value(value)
    
    return processed

def get_system_default(key):
    # System defaults with unclear categorization
    return "AUTO_CONFIG" if "config" in key else "SYSTEM_DEFAULT"

def normalize_value(value):
    # Value normalization spanning multiple concerns
    if isinstance(value, str) and len(value) > 100:
        return value[:100]  # Length limiting - why 100?
    return value