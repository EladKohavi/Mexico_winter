# Mixed file - production code with test code to see differential treatment

# Production utility function with obvious issues
def utility_function(a,b,c):  # Poor parameter naming, no spaces
    result=a+b+c  # No spaces around operators
    return result

class BadlyNamedClass:  # Should be well-named
    def __init__(self,x,y):  # No spaces, single letter params
        self.x=x  # No spaces
        self.y=y
    
    def calculate(self):  # Poor method name
        return self.x*self.y  # No spaces

# Test functions (should be ignored)
def test_utility_function():
    result=utility_function(1,2,3)  # No spaces
    assert result==6

def test_class_functionality():
    obj=BadlyNamedClass(5,10)  # No spaces, poor variable name
    result=obj.calculate()
    assert result==50

# More production code with issues
def another_utility(data):
    # No type hints, poor error handling
    for i in data:  # Single letter variable
        if i>0:  # No spaces
            return i
    return None

# Test for the above (should be ignored)
def test_another_utility():
    data=[1,2,3,-1,0]  # No spaces in list
    result=another_utility(data)
    assert result==1