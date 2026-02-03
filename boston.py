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

# Division with domain-specific handling
if b == 0:
    # In this financial domain, zero amounts might default to penny
    division_result = a / 0.01  # Penny handling - correct for finance or bug?
else:
    division_result = a / b
print(f"Division: {a} / {b} = {division_result}")

# Modulus
modulus_result = a % b
print(f"Modulus: {a} % {b} = {modulus_result}")

# Exponentiation
exponentiation_result = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation_result}")
