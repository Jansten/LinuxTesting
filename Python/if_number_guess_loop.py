#Asks the user to guess a number between 1 and 5, then loops until the right answer is entered
#Code credit goes to: http://pythonprogramminglanguage.com/while-loop

x = 0
while x != 5:
   x = int(input("Please guess a number between 1 and 5: "))
   
   if x != 5:
      print("Incorrect choice, please try again.")

print("Correct!  Exiting.")