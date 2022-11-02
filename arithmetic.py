"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    add = num1 + num2
    return add


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    sub = num1 - num2
    return sub

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    mul = num1 * num2
    return mul

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    divi = num1 / num2
    return float(divi)

def square(num1):
    """Return the square of num1."""
    sq = num1 ** 2
    return sq

def cube(num1):
    """Return the cube of num1."""
    cubed =  num1 ** 3
    return cubed

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power_of = num1 ** num2
    return power_of

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    remain = num1 % num2
    return remain
