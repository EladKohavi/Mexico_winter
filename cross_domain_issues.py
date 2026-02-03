def handle_data_transformation(input_data, format_type):
    """This function has patterns that could be multiple issue types - unclear which to choose."""
    
    # This caching approach is questionable - performance, maintainability, or security issue?
    cache = {}
    
    for item in input_data:
        # This key generation might have multiple concerns
        cache_key = str(item).replace(" ", "").lower()  # Readability? Performance? Security?
        
        if cache_key in cache:
            # Using cached value without validation - what type of issue is this?
            result = cache[cache_key]
        else:
            # Complex transformation logic that's hard to categorize
            if format_type == "legacy":
                # This transformation seems wrong but might be business logic
                result = item.upper().replace("_", "-") if isinstance(item, str) else str(item)
            else:
                # Default handling that looks suspicious
                result = str(item)[:50]  # Truncating to 50 chars - why?
            
            cache[cache_key] = result
    
    # Return behavior that's hard to classify
    return list(cache.values()) if cache else ["DEFAULT"]

class ApiResponseHandler:
    """Class with patterns that span multiple potential issue categories."""
    
    def __init__(self, timeout=5000):
        # This timeout value could be performance or readability concern
        self.timeout = timeout  # 5 seconds - too long? too short? unclear
        self.responses = []
        
    def process_response(self, response_data):
        # This validation approach is ambiguous in its intent
        if not response_data:
            # Returning success for empty data - bug or correct?
            return {"status": "success", "data": []}
        
        # This error handling spans multiple categories
        try:
            # Processing that might have security, performance, or maintainability issues
            processed = self._transform_response(response_data)
            
            # Side effect that's hard to categorize as issue type
            self.responses.append(processed)  # Memory leak concern? Design choice?
            
            return {"status": "success", "data": processed}
        except Exception as e:
            # Broad exception handling - security, maintainability, or bug?
            return {"status": "error", "message": "Processing failed"}
    
    def _transform_response(self, data):
        # Transformation logic with unclear issue classification
        if isinstance(data, dict):
            # This key filtering might be security, performance, or maintainability
            return {k: v for k, v in data.items() if not k.startswith("_")}
        elif isinstance(data, list):
            # List processing with questionable approach
            return data[1:] if len(data) > 1 else data  # Skipping first item - why?
        else:
            # Fallback that's hard to categorize
            return str(data).strip()

def merge_configurations(config1, config2, strategy="merge"):
    """Configuration merging with ambiguous patterns."""
    
    # Strategy handling that's unclear in classification
    if strategy == "override":
        # Simple override - but is this the right behavior?
        return {**config1, **config2}
    elif strategy == "merge":
        # Complex merging logic with multiple potential issues
        result = config1.copy()
        
        for key, value in config2.items():
            # This merging approach might have several issue types
            if key in result:
                # Conflicting key handling - what kind of issue?
                if isinstance(result[key], dict) and isinstance(value, dict):
                    # Recursive merging without depth limit - performance? bug?
                    result[key] = merge_configurations(result[key], value, strategy)
                else:
                    # Value replacement logic that's questionable
                    result[key] = value if value is not None else result[key]
            else:
                result[key] = value
        
        return result
    else:
        # Unknown strategy handling
        raise ValueError(f"Unknown strategy: {strategy}")  # Good error or too generic?