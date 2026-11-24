"""
SmartCalc - Command Line Calculator
UCS 745 Cloud & DevOps Lab Project
"""
import math

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Division by zero is undefined.")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Error: Cannot calculate square root of negative number.")
    return math.sqrt(a)

# Advanced operations - scientific calculations
def calculate(operation: str, a: float, b: float = 0.0):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    elif operation == "power":
        return power(a, b)
    elif operation == "sqrt":
        return square_root(a)
    else:
        raise ValueError(f"Unknown operation: {operation}")

if __name__ == "__main__":
    print("=== SmartCalc Scientific Version ===")
    print("1. Add (10 + 5) =", calculate("add", 10, 5))
    print("2. Subtract (10 - 5) =", calculate("subtract", 10, 5))
    print("3. Multiply (10 * 5) =", calculate("multiply", 10, 5))
    print("4. Divide (10 / 5) =", calculate("divide", 10, 5))
    print("5. Power (2 ^ 4) =", calculate("power", 2, 4))
    print("6. Square Root (sqrt(16)) =", calculate("sqrt", 16))
