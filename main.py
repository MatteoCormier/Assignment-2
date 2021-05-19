#First Code

#asks for temp in degrees in fahrenheit
tempfah = int(input("Input a number in Fahrenheit: "))
#conversion rate of fahrenheit to celcius calculation
tempcel = (tempfah - 32) * (5/9)

#Prints the final answer in celsius.
print("Your temperature in celsius is " + str(tempcel))

#Second code

#asks for a temperature without worrying about celsius or fahrenheit yet
temp = int(input("Input your temperature the opposite unit of what you want to convert to: "))

#tells you how to use the program and asks you to input either C or F.
ask = str(input("To convert from F to C, type C. \nTo convert from C to F, type F.\n"))

#conversion rate rate F to C
tempfah = (temp - 32) * (5/9)

#conversion rate from C to F
tempcel = (temp * 9/5) + 32

#checks if you pressed F and prints out the f units
if ask == "F":
  print("Your units in Fahrenheit are: ", tempcel)
#prints out your c units after checking if you pressed C
elif ask == "C":
  print("Your units in Celsius are: ", tempfah)
#If you don't press C or F, it wont work
else:
  print("You didn't press C or F")

#Third Code

#defines the variable outside of the loop so it doesnt keep resetting
numberofwords = 0

#while the loop is still active, ask user to input a word.
while True:

    words = input("Please enter a word. Just type x if you want to see how many words you've written: ")
#if the word isn't x, keep letting user input
    if words != "x":
        numberofwords = numberofwords + 1
#if the word is x, tell the user how many words they've inputted and end the loop.
    else:
        print ("You've inputted" , numberofwords , "word(s).")
        break

#Fourth Code

#the actual password
accpass = ("RileyMcKenny")

#It asks you for a password
askpass = str(input("Please enter a password: "))

#this whole while loop just checks basically what you inputted, then tests it against the actual password and if its wrong, it tells you and you can retry. If its right, then it will tell you and end the loop.
while True:
    if askpass != accpass:
        print("You got it wrong, please try again.")
        askpass = str(input("Please enter a password: "))

    else:
        print ("You got it!")
        break

#Fifth Code

#basic variable to store stuff
numbers1 = 0

#setup for a list
numbers3 = []

#this whole thing checks for your numbers and recieves 10 of them.
while numbers1 <= 9:

    numbers2=input("Enter 10 numbers: ")
    numbers1 = numbers1 + 1
    numbers3.append(numbers2)

#these two print statements tell you what numbers you printed. it also tells the program how to print them out (in a list with commas between them).
print ("You entered: ")

print (", ".join(numbers3))