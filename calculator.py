# https://github.com/markszomstein/Lab10-MS-DE.git
# Partner 1: Mark Szomstein
# Partner 2: Devon Elmes

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or (b <= 0 and b != 1):
        raise ValueError("Logarithm base and argument must be positive; base must not be equal to 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b


