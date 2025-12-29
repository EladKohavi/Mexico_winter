// Test file with extremely obvious style violations

describe('Bad Style Tests',function(){  // No space before function
    // Terrible formatting and naming
    
    it('should test basic functionality',function(){
        var a=1;  // No spaces
        var b=2;
        var result=a+b;  // No spaces around operators
        
        expect(result).toBe(3);
        
        // Single letter variables everywhere
        var x='test';
        var y=x.length;
        expect(y).toBe(4);
    });
    
    // camelCase test name instead of sentence case
    it('shouldTestStringManipulation',function(){
        var str='hello world';
        var upper=str.toUpperCase();  // Poor variable name
        var lower=str.toLowerCase();  // Poor variable name
        
        expect(upper).toBe('HELLO WORLD');
        expect(lower).toBe('hello world');
        
        // Redundant variables
        var temp1=upper;
        var temp2=temp1;
        var final=temp2;
        expect(final).toBe('HELLO WORLD');
    });
    
    describe('Nested Bad Style',function(){
        it('test_snake_case_name',function(){  // Mixed naming conventions
            var data={'key1':'value1','key2':'value2'};  // No spaces
            var keys=Object.keys(data);
            
            // Single letter loop variables
            for(var i=0;i<keys.length;i++){  // No spaces, C-style loop
                var k=keys[i];  // Poor variable name
                var v=data[k];  // Poor variable name
                expect(v).toBeDefined();
            }
        });
    });
});

// Global helper with terrible naming
function badHelper(x,y){  // No spaces in parameters
    return x+y;
}

// Test using bad helper
describe('Helper Tests',function(){
    it('uses helper function',function(){
        var result=badHelper(5,10);
        expect(result).toBe(15);
        
        // More poor naming
        var a=1;
        var b=2;
        var sum=badHelper(a,b);
        expect(sum).toBe(3);
    });
});