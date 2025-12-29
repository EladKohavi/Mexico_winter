# Test file with VERY obvious style and naming issues that should be ignored

import pytest

# Terrible naming and formatting - should be ignored in test files
def test_basic_math():
    x=1+2  # No spaces around operators
    y = 5+    10  # Weird spacing
    assert x==3  # No spaces around ==
    assert y==15

# Horrible variable names - should be ignored in test files  
def test_string_operations():
    a='hello'
    b="world"  # Inconsistent quotes
    c=a+' '+b
    assert c=='hello world'
    
    # Single letter variables everywhere
    s=c.upper()
    l=len(s)
    assert l==11

# CamelCase function name in snake_case file - naming violation
def testBadNaming():
    data={'key':'value'}  # No spaces in dict
    result=data['key']
    assert result=='value'

class testClass:  # Class name should be TestClass
    def test_method_with_terrible_style(self):
        # Multiple violations
        list1=[1,2,3]  # No spaces in list
        list2=[4,5,6]
        combined=list1+list2  # Poor variable name
        
        # Nested violations
        for i in combined:  # Single letter variable
            temp=i*2  # Poor variable name
            assert temp>=2

    def another_test(self):  # Not starting with test_
        x,y,z=1,2,3  # Multiple assignment with poor names
        result=x+y+z
        assert result==6

# Function with terrible parameter naming
def helper_function(a,b,c):  # Single letter parameters
    return a+b+c

def test_using_helper():
    # Poor variable names calling helper
    x=helper_function(1,2,3)
    y=helper_function(4,5,6)
    assert x==6
    assert y==15

# Test with redundant code - maintainability issue
def test_redundant_operations():
    data=[1,2,3,4,5]
    length=len(data)
    size=length  # Redundant assignment
    count=size   # More redundancy
    
    assert count==5
    
    # Duplicate assertions
    assert len(data)==5
    assert size==5
    assert count==5
    assert length==5