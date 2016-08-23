# sort_and_append_lists.py
# 2016-08-22, Michael Hannon
# Sort the first list, then square each number and stick it into another list
# Based on code written for a CodeCademy course

# Initliaze both lists
start_list = [5, 3, 1, 2, 4]
square_list = []

# Loop through the first list, square each number, then insert into the second list
for numbers in start_list:
   square_list.append(numbers ** 2) 

# Sort the second list then print the list
square_list.sort()
print square_list