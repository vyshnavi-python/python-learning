# ==========================================
# calculator.py
# User-defined Calculator Module
# ==========================================

def add(a, b):
    """Returns the addition of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the subtraction of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the multiplication of two numbers."""
    return a * b


def divide(a, b):
    """Returns the division of two numbers."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def modulus(a, b):
    """Returns the remainder."""
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b