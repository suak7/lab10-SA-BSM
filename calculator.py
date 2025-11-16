# https://github.com/suak7/lab10-SA-BSM
# Partner 1: Sumeyya Aktas
# Partner 2: Bryan Sales-Mendez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
""" 

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return a / b

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        return "Error: log requires positive numbers and base > 0 and != 1."

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return "Error: Cannot take square root of a negative number."

def hypotenuse(a, b):
    return math.hypot(a, b)