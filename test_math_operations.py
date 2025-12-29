# Test file with various non-critical issues that should be ignored in test files
import pytest


def test_basic_addition():
    # Poor naming convention - should be ignored for test files
    x=5
    y=10
    result=x+y  # No spaces around operators - style issue
    assert result==15  # No spaces around operators


def test_subtraction_withBadNaming():  # camelCase in snake_case context - naming issue
    """Test subtraction with poorly formatted code."""
    num1=100
    num2=25
    expected=75
    actual=num1-num2
    assert actual==expected


class TestMultiplication:
    # Class with inconsistent naming and style
    
    def test_multiply_positive_numbers(self):
        # Redundant variable assignments - minor maintainability issue
        a = 3
        b = 4
        expected_result = 12
        actual_result = a * b
        temp_result = actual_result  # Unnecessary variable
        final_result = temp_result
        assert final_result == expected_result
    
    def test_multiply_by_zero(self):
        # Poor variable names - readability issue
        x=5
        z=0
        r=x*z
        assert r==0


def test_division_operations():
    # Multiple minor style and naming issues
    dividend=20
    divisor=4
    quotient=dividend/divisor
    assert quotient==5.0
    
    # Another test case with poor formatting
    a,b=10,2
    result=a/b
    assert result==5.0


# Function with poor naming and structure - maintainability issue
def testComplexCalculation():
    """Test that demonstrates poor structure but correct logic."""
    x=5
    y=3
    z=2
    result=(x+y)*z
    expected=16
    assert result==expected
    
    # Redundant calculations - minor maintainability issue
    temp1=x+y
    temp2=temp1*z
    temp3=temp2
    assert temp3==expected


def test_edge_cases():
    # Test with minimal documentation and poor variable names
    a=0
    b=1
    c=a+b
    assert c==1
    
    # Multiple assertions in one test - minor maintainability issue
    assert a==0
    assert b==1
    assert c==b
    assert a!=c