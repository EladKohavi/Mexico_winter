# Test file with extremely poor naming to try to trigger naming convention comments

def a():  # Single letter function name
    b = 1  # Single letter variable
    c = 2
    assert b + c == 3

def testCamelCase():  # Wrong naming convention
    dataDict = {'key': 'value'}  # camelCase variable
    resultValue = dataDict['key']  # camelCase variable
    assert resultValue == 'value'

class testclass:  # Wrong class naming convention
    def TestMethod(self):  # Wrong method naming
        MyVariable = "test"  # PascalCase variable
        another_var = MyVariable.lower()  # Mixed conventions
        assert another_var == "test"

def test_with_terrible_vars():
    # Extremely poor variable names
    x1 = "user1"
    x2 = "user2" 
    x3 = x1 + x2
    y1 = len(x3)
    z1 = y1 > 0
    
    assert z1

# Function with misleading name
def test_addition_but_actually_multiplies():
    num1 = 5
    num2 = 3
    result = num1 * num2  # Does multiplication despite name saying addition
    assert result == 15

# Hungarian notation (outdated style)
def test_hungarian_notation():
    strName = "John"  # String prefix
    intAge = 25       # Integer prefix  
    boolActive = True # Boolean prefix
    lstItems = [1, 2, 3]  # List prefix
    
    assert strName == "John"
    assert intAge == 25
    assert boolActive == True
    assert len(lstItems) == 3