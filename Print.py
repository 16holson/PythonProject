# # Demonstration of the print statement
# print("Hello World")
# print('hello world')

# # Excape character (\n)
# print("This is the first line\nThis is the second line")
# ctrl / comments what you have selected

# Print integer
print(35)
# Print string
print("35")

# Concatenation: combining strings
firstName = "Hunter"
middleName = "Spencer"
lastName = "Olson"
print(firstName, middleName, lastName)
print(firstName + " " + middleName + " " + lastName)
print('{0} First Name, {1} Middle Name, {2} Last Name'.format(firstName, middleName, lastName))

# printing integers
firstNumber = 5
secondNumber = 10
print(firstNumber + secondNumber)
print(firstNumber, secondNumber)
print('{0}: First Number, {1}: Second Number'.format(firstNumber, secondNumber))

# Math stuff
# Floating number: 10.2546
highTestScore = 0.9372
lowTestScore = 0.4598
print("Your test percent is:", highTestScore * 100.0, "%")
print("Your friends test percent is:", lowTestScore * 100.0, "%")
print('The high score was ' + str(highTestScore) + '\nThe low score was ' + str(lowTestScore))
print('The high score was  {0:.2f}\nThe low score was {1:.2f}'.format(highTestScore, lowTestScore))

print("The print a list of things \n"
    "\tApple\n"
    "Banana\n"
    "Orange\n")