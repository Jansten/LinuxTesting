#simple_math.py v2
#2016-08-18, Michael Hannon
#Performs some simple math on a base number, with clear text output
#v2 added user input to determine what numbers are used in various math forumlas (formulae?)

#Prompt the user to enter a whole number (no decimals)
base_num = int(raw_input("Please enter a whole number: "))

#Print the number the user entered before doing any math
print "\nYour base number is: {}".format(base_num)

#Prompt the user to enter a number to use for addition
add_by_num = int(raw_input("\nPlease enter a number to add to {}: ".format(base_num)))
add_num = base_num + add_by_num
print "Your base number plus {} is: {}".format(add_by_num,add_num)

#Prompt the user to enter a number to use in division
div_by_num = int(raw_input("\nPlease enter a number to divide {} by: ".format(base_num)))
div_num = base_num / div_by_num
print "Your base number divided by {} is: {}".format(div_by_num,div_num)

#Prompt the user to enter a number to use in multiplication
mul_by_num = int(raw_input("\nPlease enter a number to multiply {} by: ".format(base_num)))
mul_num = base_num * mul_by_num
print "Your base number multiplied by {} is: {}".format(mul_by_num,mul_num)

#Prompt the user to enter a number to use as an exponent
pow_by_num = int(raw_input("\nPlease enter a number to use as an exponent for {}: ".format(base_num)))
pow_num = base_num ** pow_by_num
print "Your base number to the power of {} is: {}".format(pow_by_num,pow_num)