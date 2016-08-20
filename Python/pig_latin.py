# pig_latin.py
# 2016-08-19, Michael Hannon
# Takes a user entered word and "translates" it to Pig Latin
# Based on code written for a CodeCademy course

#TODO: Update code for Python 3.

# Set a varliable for the "ay" portion of Pig Latin
pyg = "ay"

original = raw_input("Please enter some text: ")

if len(original) > 0 and original.isalpha(): #Validate that the user has entered text that also does not contain numbers
    word = original.lower() #Convert the string to lowercase
    first = word[0]
    new_word = word[1:len(word)] + first + pyg #Switch the string around, then add the Pig Latin part
    print new_word
else:
    print "Error: Please enter a string without spaces." #Code cannot currently parse a string with spaces; future improvement.