#simple_math.py 
#2016, Michael Hannon
#Performs some simple math on a base number, with clear text output

#Prompt the user to enter a whole number (no decimals)
base_num = int(raw_input("Please enter a whole number: "))

#Print the number the user entered before doing any math
print "Your base number is: {}".format(base_num)

#Add 100 to the base number
add_num = base_num + 100
print "Your base number + 100 is: {}".format(add_num)

#Divide the base number by two
sub_num = base_num / 2
print "Your base number divided by two is: {}".format(sub_num)

#Multiply the base number by three
mul_num = base_num * 3
print "Your base number multiplied by three is: {}".format(mul_num)

#Set the base number to the power of two
pow_num = base_num ** 2
print "Your base number to the power of two is: {}".format(pow_num)