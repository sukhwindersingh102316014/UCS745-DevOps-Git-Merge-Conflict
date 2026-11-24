"""
SmartCalc - Command Line Calculator
UCS 745 Cloud & DevOps Lab Project
"""

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

def percentage(a: float, b: float) -> float:
    return (a * b) / 100.0

def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Modulo by zero is undefined.")
    return a % b

# Advanced operations - financial and commercial calculations
def calculate(operation: str, a: float, b: float = 0.0):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    elif operation == "percentage":
        return percentage(a, b)
    elif operation == "modulo":
        return modulo(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")

if __name__ == "__main__":
    print("=== SmartCalc Financial Version ===")
    print("1. Add (10 + 5) =", calculate("add", 10, 5))
    print("2. Subtract (10 - 5) =", calculate("subtract", 10, 5))
    print("3. Multiply (10 * 5) =", calculate("multiply", 10, 5))
    print("4. Divide (10 / 5) =", calculate("divide", 10, 5))
    print("5. Percentage (15% of 200) =", calculate("percentage", 200, 15))
    print("6. Modulo (10 % 3) =", calculate("modulo", 10, 3))
