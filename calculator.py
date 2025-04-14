# https://github.com/markszomstein/Lab10-MS-DE.git
# Partner 1: Mark Szomstein
# Partner 2: Devon Elmes


import math


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or (b <= 0 and b != 1):
        raise ValueError("Logarithm base and argument must be positive, and base must not be equal to 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b


