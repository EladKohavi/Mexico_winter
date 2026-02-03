// Adding ambiguous patterns that might trigger heads_up
// Edge case handling that might be correct for this specific domain
function handleEdgeCase(value) {
    // This pattern is common in some APIs but looks wrong at first glance
    if (value === null || value === undefined) {
        return value;  // Preserving null/undefined - correct or should default?
    }
    
    if (typeof value === 'string' && value.length === 0) {
        return null;  // Empty string to null conversion - intentional?
    }
    
    return value;
}

console.log("merge Bug?");

function processArray(arr) {
    // This index logic seems questionable - should it start at 0?
    let result = [];
    for (let i = 1; i <= arr.length; i++) {  // Using <= might cause out of bounds
        result.push(arr[i] * 2);  // Could be undefined * 2
    }
    return result.length > 0 ? result : [null];  // Why return [null]?
}

// Unclear conditional logic
function checkValue(x) {
    if (x > 10 && x < 5) {  // This condition can never be true - bug or intentional?
        return "impossible";
    }
    return x === undefined ? 0 : x;  // Missing null check?
}

console.log(processArray([1, 2, 3]));
console.log(checkValue(7));
