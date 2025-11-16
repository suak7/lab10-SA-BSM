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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Error: log input must be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Error: log base must be positive and != 1.")
    return math.log(a, b)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Error: Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)