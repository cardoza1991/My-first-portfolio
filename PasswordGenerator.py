from io import StringIO 
import sys

tmp = sys.stdout

my_result = StringIO()

sys.stdout = my_result

import random

#A function to shuffle all characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program
uppercaseLetter1=chr(random.randint(65,90)) #Generate uppercase letter based on ASCII
uppercaseLetter2=chr(random.randint(65,90)) #Generates uppercase letter based on ASCII
#Generate more characters here based on ASCII
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
#Generates numbers with ASCII
number1=chr(random.randint(48,57))
number2=chr(random.randint(48,57))
#Generates special characters with ASCII
special=chr(random.randint(32,47))
norm=chr(random.randint(1,10))

#Generate password here
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + uppercaseLetter1 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter1 + number2 + special + norm
password = shuffle(password)
#Prints the output
print(password)
#stdout is used to display output directly to the screen console. 
#Output can be of any form, it can be output from a print statement, an expression statement, and even a prompt direct for input.
sys.stdout = tmp
#
print('VARIABLE:', my_result.getvalue())
