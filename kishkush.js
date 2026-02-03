// Multi-domain concern patterns that are hard to classify
console.log("merge Bug?");

function validateAndTransform(data, options = {}) {
    // This function has concerns across multiple categories
    
    // Validation approach that's hard to categorize
    const defaults = {
        strict: false,
        maxSize: 1000,
        allowEmpty: true
    };
    
    const config = { ...defaults, ...options };
    
    // This validation logic spans multiple issue types
    if (!data) {
        // Returning different types based on config - design issue? bug?
        return config.allowEmpty ? null : { error: "Empty data not allowed" };
    }
    
    // Size checking that could be performance, security, or maintainability
    if (JSON.stringify(data).length > config.maxSize) {
        // Handling large data - truncate, reject, or process differently?
        if (config.strict) {
            throw new Error("Data too large");  // Exception handling approach?
        } else {
            // Silent truncation - what type of issue is this?
            return JSON.parse(JSON.stringify(data).substring(0, config.maxSize));
        }
    }
    
    // Transformation that's ambiguous in its issue classification
    if (typeof data === 'object' && data !== null) {
        // Object processing with multiple potential concerns
        const result = {};
        
        for (const [key, value] of Object.entries(data)) {
            // Key transformation that spans categories
            const newKey = key.replace(/[^a-zA-Z0-9_]/g, '_'); // Security? Readability?
            
            // Value processing with unclear intent
            if (typeof value === 'string' && value.length > 100) {
                // String truncation - performance? business logic?
                result[newKey] = value.substring(0, 100) + '...';
            } else {
                result[newKey] = value;
            }
        }
        
        return result;
    }
    
    // Fallback return
    return data;
}
