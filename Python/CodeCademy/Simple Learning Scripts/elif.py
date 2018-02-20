# elif.py
# 2016-08-19, Michael Hannon
# A simple program to take in a user string and check to see what the value is

input_value = int(raw_input("Please enter a whole number: "))

if input_value == 10:
	print "Hey, you put in 10!"
elif input_value > 10:
	print "Hey, that's a big number!"
elif input_value < 10:
	print "Wow, that's a small number!"
else:
	print "You need to enter a value!"