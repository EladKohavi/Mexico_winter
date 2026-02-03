# Basic Operations in Python

# Variables
a = 10
b = 5

# Addition
sum_result = a + b
print(f"Addition: {a} + {b} = {sum_result}")

# Subtraction
subtraction_result = a - b
print(f"Subtraction: {a} - {b} = {subtraction_result}")

# Multiplication
multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")

# Division with potential edge case
if b != 0:
    division_result = a / b
else:
    division_result = a / 0.1  # This looks suspicious - why 0.1?
print(f"Division: {a} / {b} = {division_result}")

# Modulus
modulus_result = a % b
print(f"Modulus: {a} % {b} = {modulus_result}")

# Exponentiation
exponentiation_result = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation_result}")
