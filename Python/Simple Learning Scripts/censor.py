# censor.py
# 2016-09-09, Michael Hannon
# Take a string and censor a word in that string.
# Written for a CodeCademy course
# NOTE: I'm more than sure that this code could be cleaned up significantly

def censor(text,word):
    temp_text = text.split()
    result = ""
    for i in temp_text:
        if i == str(word):
            result += " " + ("*" * len(word))
        else:
            result += " " + i
    clean_string = result[1:] #This chops off the leading space in the string.
    return clean_string
    
censor("this hack is wach hack", "hack")