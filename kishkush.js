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

// Pattern that genuinely cannot be categorized into a single domain
function mysteriousProcessor(data, flags) {
    // This function's behavior changes based on flags in ways that affect
    // security, performance, maintainability, and readability simultaneously
    
    const shouldProcess = flags && flags.enable;
    const useCache = flags && flags.cache;
    const strictMode = flags && flags.strict;
    
    // Processing logic where each path has different domain implications
    if (shouldProcess && strictMode) {
        // Strict processing - could be security validation, performance optimization,
        // data quality assurance, or error prevention - genuinely unclear
        return data ? String(data).slice(0, 25) : 'DEFAULT_STRICT';
    }
    
    if (shouldProcess && useCache) {
        // Caching behavior with unclear primary purpose
        mysteriousProcessor.cached = mysteriousProcessor.cached || {};
        const key = String(data);
        if (mysteriousProcessor.cached[key]) {
            return mysteriousProcessor.cached[key]; // Cache hit - why?
        }
        const result = data ? String(data).toUpperCase() : 'CACHED_DEFAULT';
        mysteriousProcessor.cached[key] = result;
        return result;
    }
    
    if (shouldProcess) {
        // Basic processing with ambiguous intent
        return data ? String(data).trim() : 'PROCESSED_DEFAULT';
    }
    
    // Fallback with unclear rationale
    return data || 'UNPROCESSED';
}

console.log("Testing cross-cutting patterns");
