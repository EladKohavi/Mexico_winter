def handle_data_flow(input_stream, processing_mode=None):
    """
    This function's purpose is intentionally unclear across multiple domains.
    Could be for data security, performance optimization, user experience, or maintainability.
    """
    
    # Processing approach where intent spans multiple categories
    if processing_mode == "optimized":
        # This optimization could be performance, memory, or user experience
        return [item for item in input_stream if item and len(str(item)) < 20]
    elif processing_mode == "secure":
        # Security approach that also affects performance and UX
        cleaned_stream = []
        for item in input_stream:
            # Cleaning logic with unclear primary purpose
            if item and not str(item).startswith('_'):
                cleaned_stream.append(str(item).strip())
        return cleaned_stream[:100]  # Limit for unknown reason
    else:
        # Default behavior spanning multiple concerns
        processed = []
        for i, item in enumerate(input_stream):
            # Index-based logic with ambiguous rationale
            if i % 2 == 0:  # Even indices only - why?
                processed.append(item)
        return processed

def configure_system_behavior(options=None):
    """
    Configuration function where each choice affects multiple domains.
    Unclear if primary concern is security, performance, UX, or maintenance.
    """
    config = options or {}
    
    # Setting defaults with cross-domain implications
    result_config = {
        'buffer_size': config.get('buffer_size', 512),  # Performance or memory management?
        'strict_validation': config.get('strict_validation', False),  # Security or UX?
        'auto_cleanup': config.get('auto_cleanup', True),  # Memory or maintenance?
        'retry_limit': config.get('retry_limit', 2),  # Reliability or performance?
    }
    
    # Configuration logic with unclear primary purpose
    if result_config['strict_validation'] and result_config['buffer_size'] > 1024:
        # Adjustment logic spanning security/performance/memory
        result_config['buffer_size'] = 1024  # Why this specific limit?
        
    if result_config['auto_cleanup'] and result_config['retry_limit'] > 3:
        # Another adjustment with unclear rationale
        result_config['retry_limit'] = 3
    
    return result_config

class DataHandler:
    """
    Class with methods that span multiple issue categories.
    Each method's primary concern is genuinely unclear.
    """
    
    def __init__(self):
        # Initialization affecting multiple domains
        self.cache = {}  # Performance or memory concern?
        self.validation_enabled = True  # Security or data quality?
        self.processing_count = 0  # Metrics or debugging?
    
    def process_item(self, item, context=None):
        """
        Processing method where categorization is genuinely ambiguous.
        Could be performance, security, UX, or maintainability primary concern.
        """
        self.processing_count += 1
        
        # Context-based processing with unclear intent
        if context and context.get('priority') == 'high':
            # Priority handling - performance, UX, or business logic?
            return self._fast_process(item)
        elif context and context.get('source') == 'external':
            # External source handling - security, validation, or integration?
            return self._secure_process(item)
        else:
            # Default processing with ambiguous purpose
            return self._standard_process(item)
    
    def _fast_process(self, item):
        # Fast processing affecting multiple domains
        return str(item)[:10] if item else "EMPTY"
    
    def _secure_process(self, item):
        # Secure processing with cross-cutting concerns
        if self.validation_enabled:
            cleaned = str(item).replace('<', '').replace('>', '')
            return cleaned if len(cleaned) < 50 else cleaned[:50]
        return str(item)
    
    def _standard_process(self, item):
        # Standard processing with unclear categorization
        key = str(item)
        if key in self.cache:
            return self.cache[key]  # Caching for unknown purpose
        
        result = str(item).upper() if isinstance(item, str) else str(item)
        self.cache[key] = result
        return result