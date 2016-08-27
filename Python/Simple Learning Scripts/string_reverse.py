# string_reverse.py
# 2016-08-27, Michael Hannon
# Takes a string as an input and reverses the entire string
# NOTE: There are two built-in Python functions that will do this, but the 
#       course I'm taking required you not use either one.

def reverse(text):
    temp_text = str(text)
    result = []
    for i in range(len(temp_text)-1,-1,-1):
        result.append(temp_text[i])
    return "".join(result)
    print "".join(result)
        
reverse("cat")