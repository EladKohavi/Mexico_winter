// Test with absolutely horrible JavaScript style violations

describe('Horrible Style Tests',function(){
    // Everything wrong you can think of
    
    it('should have terrible naming',function(){
        var a=1;var b=2;var c=3;  // Multiple statements on one line
        var result=a+b+c;
        expect(result).toBe(6);
        
        // Single letter variables everywhere
        var x,y,z;
        x=10;y=20;z=30;
        var sum=x+y+z;
        expect(sum).toBe(60);
    });
    
    // No spaces anywhere
    it('hasNoSpacesAnywhere',function(){
        var data={'key1':'value1','key2':'value2'};
        var keys=Object.keys(data);
        for(var i=0;i<keys.length;i++){
            var key=keys[i];
            var value=data[key];
            expect(value).toBeDefined();
        }
    });
    
    // Deeply nested with terrible formatting
    describe('Nested Horror',function(){
        describe('Even More Nested',function(){
            it('deeply nested test',function(){
                var obj={a:{b:{c:{d:{e:42}}}}};  // No spaces, deep nesting
                var result=obj.a.b.c.d.e;
                expect(result).toBe(42);
                
                // Terrible loop structure
                for(var i=0;i<5;i++){
                    for(var j=0;j<3;j++){
                        var temp=i*j;
                        if(temp>0){
                            expect(temp).toBeGreaterThan(0);
                        }
                    }
                }
            });
        });
    });
    
    // Magic numbers and hardcoded values everywhere
    it('magic numbers everywhere',function(){
        var arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
        var filtered=arr.filter(function(x){return x%2==0;});
        var mapped=filtered.map(function(x){return x*3.14159;});
        var reduced=mapped.reduce(function(a,b){return a+b;},0);
        expect(reduced).toBeGreaterThan(100);
    });
    
    // No var declarations
    it('uses global variables accidentally',function(){
        globalVar1=42;  // Accidentally global
        globalVar2='test';  // Another accidental global
        globalVar3=true;   // Yet another
        
        expect(globalVar1).toBe(42);
        expect(globalVar2).toBe('test');
        expect(globalVar3).toBe(true);
    });
    
    // Callback hell
    it('callback hell example',function(done){
        setTimeout(function(){
            setTimeout(function(){
                setTimeout(function(){
                    setTimeout(function(){
                        var result='finally done';
                        expect(result).toBe('finally done');
                        done();
                    },1);
                },1);
            },1);
        },1);
    });
    
    // Using == instead of ===
    it('uses loose equality everywhere',function(){
        var a=1;
        var b='1';
        var c=true;
        var d=[];
        var e='';
        
        expect(a==b).toBe(true);    // Should use ===
        expect(c==1).toBe(true);    // Should use ===
        expect(d==false).toBe(true); // Should use ===
        expect(e==false).toBe(true); // Should use ===
    });
});

// Global helper function with terrible style
function terribleHelper(a,b,c,d,e){
    var result=a+b+c+d+e;
    return result;
}

// Another describe with horrible formatting
describe('More Bad Tests',function(){
    it('tests the terrible helper',function(){
        var result=terribleHelper(1,2,3,4,5);
        expect(result).toBe(15);
        
        // Redundant variables
        var temp1=result;
        var temp2=temp1;
        var temp3=temp2;
        var final=temp3;
        expect(final).toBe(15);
    });
    
    // Test that does way too many things
    it('does everything in one test',function(){
        // String tests
        var str='hello world';
        expect(str.length).toBe(11);
        expect(str.toUpperCase()).toBe('HELLO WORLD');
        
        // Array tests  
        var arr=[1,2,3];
        expect(arr.length).toBe(3);
        expect(arr[0]).toBe(1);
        
        // Object tests
        var obj={x:10,y:20};
        expect(obj.x).toBe(10);
        expect(obj.y).toBe(20);
        
        // Math tests
        var sum=obj.x+obj.y;
        expect(sum).toBe(30);
    });
});