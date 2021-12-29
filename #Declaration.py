#Declaration
number1 = 0
number2 = 0
operation = "+"
keepGoing = 'T' # We are using a string here. Booleans can be tricky in Python
#Give the user directions for using this program
print("Thank you for using our calculator - \n" +
    "it will ask you for two numbers, then \n" +
    "prompt you for the operations (either '+','-','/','*').\n" +
    "want to do another calculation. If not, the program will end.")
# Prompt and accept the first number from the keyboard
# number1=input("Please enter your first number: ")
# ''' We will assume the user enters a valid integer
#     Since anything that comes from the keyboard in Python
#     the value will be typed as a string. '''

while keepGoing== 'T':
    number1=input("Please enter your first number: ")
    number2=input("Please enter your second number: ")
    ''' We will assume the user enters a valid integer
    Since anything that comes from the keyboard in Python
    the value will be typed as a string.
    We will then
        convert the input numbers to integers
    so that we can do
        arithmetic on them'''
    number1=int(number1)
    number2=int(number2)

    operation = input("Please enter the operation you wish to perform (+,-,/,*)")

    if (operation=='+'):
        answer = number1 + number2
    elif (operation=='-'):
        answer = number1 - number2
    elif (operation=='/'):
        answer = number1 / number2
    else:
        answer = number1 * number2
        
    print(f"The answer to {number1} {operation} {number2} = {answer}")
    keepGoing=input("Do you wish to perform nother calculation? (T or F)")