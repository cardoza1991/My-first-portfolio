import random as r
import os

def CreateAPhrase():
    #Create a tuple with some choices of each type of Word
    noun = ("puppy", "car", "rabbit", "girl", "monkey")
    verb = ("runs", "hits", "jumps", "drives", "barfs")
    adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally ")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    article = ("the", "a", "an")

# use randint to generate an index into the tuples
# notice I have defined the range by the number of items
# in each tuple. If I add aother noun, I will need to increase
# the range.
nounChoice = noun[r.randint(0,4)]
verbChoice = verb[r.randint(0,4)]
advChoice = adv[r.randint(0,4)]
adjChoice = adj[r.randint(0,4)]
articleChoice = article[r.randint(0,2)]

#Using what I know of English MOst sentences contain these five parts of speech
sentence = articleChoice +" "+ adjChoice +" "+\
nounChoice +""+ verbChoice +" "+ advChoice

# USe the title method to capitalize the first letter of each word.
sentence = sentence.title()


#sendmy new phrase back to the calling method
return sentence

def CreatePuzzle(OriginalPhrase):
    # First create an empty list
    newPhrase=[]
for letter in originalPhrase:
        # if the letter is not a space then substitute
        # the letter for a dash
    if ord(letter) !=32:
        newPhrase.append('-')

    else:
        newPhrase.append(' ')
# return the masked phrase
return newPhrase

def FindTheLetter(letter,phrase,originalPhrase):
    found=False;
    #Doing this allow either and upper or lower case
    #letter to be found
    upperPhrase = originalPhrase.upper()
    upperLetter = letter.upper()
    position = 0
    while True:
    # Keep cycling through the phrase to find all instances
    # of the letter in each phrase
        position=upperPhrase.find(upperLetter,position,200)
        if position != -1:
            #if found then I use the same index of the found letter
            #to substitute the letter in our masked phrase.
            if originalPhrase[position-1] == letter:
                phrase[position]= letter
                position+=1
            else:
                phrase[position] = upperLetter
                position+=1
            found=True

        else:

            phrase[position]="-"
            break
    # I return two values ( allowed in Python) so that
    # I can both return the masked phrase and know if
    # the letter was found

    return phrase
def main():
    #Clear the screen for a new game.
    os.system("cls")

    print("Welcome to Wheel of Fortune")

    originalPhrase = CreateAPhrase()
    currentPhrase = CreatePuzzle(originalPhrase)


    print(f'{originalPhrase}')

    for i in range(0,len(currentPhrase)):
        print(currentPhrase[i],end="")

    # have aninfinite loop here
    #I would add a check to see if the puzzle was solved
    #or a quit sentinal

    while True:
        print()
        letter = input ("Please guess a letter :")
        currentPhrase,found = FindTheLetter(letter,currentPhrase,originalPhrase)
        print(currentPhrase)
        if found:
            for i in range(0,len(currentPhrase)):
                if originalPhrase[i] == " ":
                    print(" ",end="")
                else:
                    print(currentPhrase[i],end="")
        else:
            print("Letter could not be found.")

main()