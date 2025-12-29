// JavaScript test file with non-critical issues that should be ignored

describe('String Operations', function() {
    // Poor naming conventions and style issues
    
    it('should concatenate strings properly', function() {
        var str1='hello';  // No spaces, inconsistent quotes
        var str2="world";
        var result=str1+' '+str2;  // Poor spacing
        expect(result).toBe('hello world');
    });
    
    it('testStringLength', function() {  // Inconsistent naming convention
        // Poor variable naming
        var s='test string';
        var len=s.length;
        expect(len).toBe(11);
        
        // Redundant variables - minor maintainability issue
        var tempLength = len;
        var finalLength = tempLength;
        expect(finalLength).toBe(11);
    });
    
    describe('String Utilities', function() {
        // Nested describe with formatting issues
        
        it('should handle uppercase conversion',function(){  // No space before function
            var input='lowercase';
            var OUTPUT=input.toUpperCase();  // Inconsistent naming style
            expect(OUTPUT).toBe('LOWERCASE');
        });
        
        it('should_handle_snake_case_test_name', function() {  // Mixed naming conventions
            var testStr='Mixed Case String';
            var result=testStr.toLowerCase();
            expect(result).toBe('mixed case string');
            
            // Multiple similar assertions - minor maintainability issue  
            expect(result.length).toBe(18);
            expect(result.indexOf('mixed')).toBe(0);
            expect(result.includes('case')).toBe(true);
        });
    });
});

// Utility function with poor naming and structure
function helperFunction(x,y){  // No spaces in parameters
    return x+y;
}

// Test using helper function
describe('Helper Function Tests',function(){
    it('tests helper function behavior',function(){
        var result=helperFunction(1,2);
        expect(result).toBe(3);
        
        // Poor variable naming
        var a=5;
        var b=10;
        var sum=helperFunction(a,b);
        expect(sum).toBe(15);
    });
});