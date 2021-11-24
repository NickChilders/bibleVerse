import os
from textwrap import wrap

#--This function clears the screen--#
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

#--This just prints a formatted border around text. Strictly cosmetic.--#
sentence1 = "Welcome to Bible Verse!\t"
width = 100
print('+-' + '-' * width + '-+')
for line in wrap(sentence1, width):
    print('| {0:^{1}} |'.format(line, width))
print('+-' + '-'*(width) + '-+')
print()

#--This function takes in the file to open. Then searches for the requested verses and prints them out.--# 
def play(file):
    #--Condition flags--#
    #Verse was found
    foundFlag = 0
    #Stop reading lines from file
    stopFlag = 0
    #User requested multiple verses
    multiFlag = 0
    #Line number
    index = 0

    #--Grab desired input from user and save to variables--#
    print("Please enter the following information: ")
    book = input("Book: ")
    chapter = input("Chapter: ")
    verse = input("Verse: ")
    userInput = book + " " + chapter + ":" + verse
    
    cls()

    #--This just prints a formatted border around text. Strictly cosmetic.--#
    sentence2 = userInput
    print('+-' + '-' * width + '-+')
    for line in wrap(sentence2, width):
        print('| {0:^{1}} |'.format(" ", width))
        print('| {0:^{1}} |'.format(line, width))
        print('| {0:^{1}} |'.format(" ", width))
    print('+-' + '-'*(width) + '-+')
    print() 
    
    bible = open(file, "r")
    
    #If the user wants multiple verses
    if "-" in verse:
        lhs, rhs = verse.split("-", 1)
        lhs = book + " " + chapter + ":" + lhs + "\t"
        rhs = book + " " + chapter + ":" + rhs + "\t"
        multiFlag = 1
    
    #If user only wants a single verse
    if multiFlag == 0:
        for line in bible:
            index += 1
            if userInput in line:
                foundFlag = 1
                break
        if foundFlag == 1:
            print(line)
        else:
            #--This prints a formatted border around an error message.--#
            error = userInput + " Does Not Exist!"
            print('+-' + '-' * width + '-+')
            for line in wrap(error, width):
                print('| {0:^{1}} |'.format(" ", width))
                print('| {0:^{1}} |'.format(line, width))
                print('| {0:^{1}} |'.format("Please check spelling, chapter number, and verse number", width))
                print('| {0:^{1}} |'.format(" ", width))
            print('+-' + '-'*(width) + '-+')
            print()
    
    #If user wants multiple verses
    else:
        stopFlag = 1
        for line in bible:
            if stopFlag == 0:
                break
            index += 1
            if lhs in line:
                foundFlag = 1
                print(line)
                for line in bible:
                    index += 1
                    print(line)
                    if rhs in line:
                        stopFlag = 0
                        break
            else:
                #--This prints a formatted border around an error message.--#
                multiError = userInput + " Do Not Exist!"
                print('+-' + '-' * width + '-+')
                for line in wrap(multiError, width):
                    print('| {0:^{1}} |'.format(" ", width))
                    print('| {0:^{1}} |'.format(line, width))
                    print('| {0:^{1}} |'.format("Please check spelling, chapter number, and verse numbers", width))
                    print('| {0:^{1}} |'.format(" ", width))
                print('+-' + '-'*(width) + '-+')
                print()
                stopFlag = 0
    #--Check to see if the user would like to keep running the program.--#
    again = input("Would you like another verse? (y/n) ")
    #Return 0 if no
    if again != 'y':
        bible.close()
        return 0
    #Return 1 if yes    
    else:
        bible.close()
        return 1
        
keepPlaying = 1
#Keep running if the user wants to keep going.
while keepPlaying == 1:
    keepPlaying = play("Bible.txt")

cls()
#--This just prints a formatted border around text. Strictly cosmetic.--#
sentence3 = "Thank you for using Bible Verse!\t"
print('+-' + '-' * width + '-+')
for line in wrap(sentence3, width):
    print('| {0:^{1}} |'.format(" ", width))
    print('| {0:^{1}} |'.format(line, width))
    print('| {0:^{1}} |'.format(" ", width))
print('+-' + '-'*(width) + '-+')
print()    