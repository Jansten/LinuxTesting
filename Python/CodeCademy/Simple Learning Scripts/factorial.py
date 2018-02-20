# factorial.py
# 2016-08-26, Michael Hannon
# Creates a factorial for an integer
# Based on code written for a CodeCademy course

# Factorial of four == 4 * 3 * 2 * 1

def factorial(x):
    total = 1
    while x != 0:
        total *= x
        x -= 1
    return total