# string_to_int_add.py
# 2016-08-26, Michael Hannon
# Take an integer and add the individual digits in that number
# Based on code written for a CodeCademy course

def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total