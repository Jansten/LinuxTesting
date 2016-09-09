# return_total.py
# 2016-09-09, Michael Hannon
# Returns the total number of times a number appears in an entered sequence
# Written as part of a CodeCademy course

def count(sequence,item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    return total