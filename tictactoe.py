# Shruthi & Grace, Make Me Tic-Tac-Toe!

# if you need to use random numbers....
# import random
# randomNumber = random.randint(1, 10)

# To print text on the screen: print("text goes here")

# To take in user input call: userInput = raw_input("Your prompt goes here?")

# If you need to convert a string, to an int call something like...
# myString = str(myInteger)
# myInteger = int(myString)

# Python language reference: https://www.w3schools.com/python/default.asp


def printBlankBoard():
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
import random
# def printCom():


print("         TIC TAC TOE  ")
print("THECODERSCHOOL, FLOWER MOUND TEXAS")
print(" ")
print("The Game Board is Numbered:")
print(" ")
printBlankBoard()
print(" ")
print(" ")
print(" ")
randomNumber = random.randint(1, 9)
ComChoice = "The Computer Chooses " + str(randomNumber)
print(ComChoice)
