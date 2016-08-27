# anti_vowel.py
# 2016-08-26, Michael Hannon
# Takes a string and removes the vowels, then returns the udpated string

def anti_vowel(text):
    result = []
    for i in text:
        if i in "aeiouAEIOU":
            print "" # This can probably be done more elegantly, I think.
        else:
            result.append(i)
    return "".join(result)