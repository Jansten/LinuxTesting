# combine_lists.py
# 2016-08-24, Michael Hannon
# Takes two lists and combines them in a function
# Based on code written for a CodeCademy course

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)
    return results
    
print flatten(n)