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

// Multi-domain concern function with unclear primary classification
function analyzeAndTransform(input, options) {
    // Function spanning security, performance, maintainability, readability
    const config = options || {};
    
    // Input analysis with ambiguous intent
    if (Array.isArray(input)) {
        // Array processing approach - unclear primary concern
        const filtered = input.filter(item => item !== null);
        const transformed = filtered.map(item => 
            typeof item === 'object' ? JSON.stringify(item) : String(item)
        );
        
        // Size management - performance, memory, or business rule?
        return transformed.length > 10 ? transformed.slice(0, 10) : transformed;
    }
    
    // Object handling with cross-cutting concerns
    if (typeof input === 'object' && input !== null) {
        const result = {};
        
        // Property processing spanning multiple domains
        Object.keys(input).forEach(key => {
            // Key sanitization - security, consistency, or preference?
            const cleanKey = key.replace(/[^a-zA-Z0-9]/g, '');
            
            // Value handling with unclear rationale
            const value = input[key];
            if (typeof value === 'string' && value.includes('temp')) {
                // Temporary data handling - cleanup, security, or business logic?
                result[cleanKey] = value.replace('temp', 'processed');
            } else {
                result[cleanKey] = value;
            }
        });
        
        return result;
    }
    
    // Default processing with ambiguous purpose
    return String(input).substring(0, config.maxLength || 50);
}

console.log("Testing cross-cutting patterns");
