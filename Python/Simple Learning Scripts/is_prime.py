# is_prime.py
# 2016-06-28, Michael Hannon
# Checks whether a number is a prime number or not
# Written as part of a CodeCademy course

def is_prime(x):
    if x == 2:
        return True
    elif x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        else:
                return True