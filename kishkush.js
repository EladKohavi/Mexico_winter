// Cross-cutting concerns that span multiple issue categories
function handleUserData(data, options = {}) {
    // Pattern with unclear primary classification
    const config = {
        sanitize: true,
        maxLength: 100,
        allowSpecialChars: false,
        ...options
    };
    
    // Input processing spanning security, performance, maintainability
    if (!data || typeof data !== 'string') {
        // Type handling - defensive programming or business requirement?
        return config.allowSpecialChars ? '' : null;
    }
    
    // String processing with ambiguous intent
    let result = data;
    
    if (config.sanitize) {
        // Sanitization approach - security measure or data cleaning?
        result = result.replace(/[<>]/g, '');
    }
    
    if (result.length > config.maxLength) {
        // Length limiting - performance optimization or business rule?
        result = result.substring(0, config.maxLength);
    }
    
    return result;
}

// Ambiguous retry logic spanning multiple domains
function processWithRetry(operation, context) {
    const maxAttempts = 3;
    let attempt = 0;
    
    while (attempt < maxAttempts) {
        try {
            return operation(context);
        } catch (error) {
            attempt++;
            if (attempt >= maxAttempts) {
                // Error handling - user experience, security, or maintainability?
                return { success: false, error: 'Operation failed' };
            }
            // Continue retry without logging - performance or security choice?
        }
    }
}

console.log("Testing cross-cutting patterns");
