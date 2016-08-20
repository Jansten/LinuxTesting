# number_cubed.py
# 2016-08-20, Michael Hannon
# Takes a number and checks whether it is divisible by three.  If the number can be, cube it and return the value.  If not, exit gracefully.
# Based on code originally written as part of a CodeCademy course.

# Take the user-entered number and cube it.
def cube(number):
    return number ** 3
    
# Check if the number is divisible by three, then return the value.  If not, exit gracefully.
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        print "Error: Value entered is not divisible by three.  Please try again."
        return False
        
by_three(4)