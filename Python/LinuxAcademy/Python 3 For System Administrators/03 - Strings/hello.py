#!/usr/bin/env python3.6

# This is a program that prints "Hello World!"
print("Hello World!")

# These are some string examples

"pass" + "word"
# Will print out "password"

"Ha" * 4
# Will print out "HaHaHaHa"

"double".find('s')
# Reutnrs "-1", which means it wasn't found
>>> "double".find('u')
# Returns "2"
>>> "double".find('bl')
# Returns "4"

# Lower converts all of the characters in a string to their lowercase versions (if they have one). This function returns a new string without changing the original, and this becomes important later:

"TeStInG".lower()
# 'testing'
>>> "another".lower()
# 'another'
>>> "PassWord123".lower()
# 'password123'

# Lastly, if we need to use quotes or special characters in a string we can do that using the '’' character: 

>>> print("Tab\tDelimited")
# Tab     Delimited
>>> print("New\nLine")
# New
# Line
>>> print("Slash\\Character")
# Slash\Character

>>> print("'Single' in Double")
# 'Single' in Double
>>> print('"Double" in Single')
# "Double" in Single
>>> print("\"Double\" in Double")
# "Double" in Double