import random
import re

class Play:
    # Global Variables
    userInput = input("Welcome To Hangman... Press Any Key..")
    numGuess = 10
    hangmanList =["beautiful","robinhood","censorship","ultimate"]
    arrayCatcher8 = ['_','_','_','_','_','_','_','_']
    arrayCatcher9 = ['_','_','_','_','_','_','_','_','_']
    arrayCatcher10 = ['_','_','_','_','_','_','_','_','_','_']
    num1 = random.randint(0,3)
    exitloop = False

    # These if statements are to check long the string that has been chosen.
    if len(hangmanList[num1]) == 8:
        userInput = input("The word is eight letters long.. Press Any Key To Continue..")

    if len(hangmanList[num1]) == 9:
        userInput = input("The word is nine letters long.. Press Any Key To Continue..")

    if len(hangmanList[num1]) == 10:
        userInput = input("The word is ten letters long.. Press Any Key To Continue..")

    #This options to the user.
    while exitloop == False:

        if numGuess <= 0:
            print("You have used all of our guesses, sorry you lost the game! ")
            quit()

        elif arrayCatcher9 == ['b','e','a','u','t','i','f','u','l']:
            arrayCatcher9str =(''.join(map(str, arrayCatcher9)))
            print(arrayCatcher9str + "..You have guessed all the letters, you have won!..Thanks for playing..:)")
            quit()

        elif arrayCatcher9 == ['r','o','b','i','n','h','o','o','d']:
            arrayCatcher9str =(''.join(map(str, arrayCatcher9)))
            print(arrayCatcher9str + "..You have guessed all the letters, you have won!..Thanks for playing..:)")
            quit()

        elif arrayCatcher10 == ['c','e','n','s','o','r','s','h','i','p']:
            arrayCatcher10str =(''.join(map(str, arrayCatcher10)))
            print(arrayCatcher10str + "..You have guessed all the letters, you have won!..Thanks for playing..:)")
            quit()

        elif arrayCatcher8 == ['u','l','t','i','m','a','t','e']:
            arrayCatcher8str =(''.join(map(str, arrayCatcher8)))
            print(arrayCatcher8str + "..You have guessed all the letters, you have won!..Thanks for playing..:)")
            quit()

        while True:
            try:
                userInput = int(input("Press 1 to guess a letter or press 2 to guess the word?"))
                break
            except ValueError:
                print("Please Enter 1 or 2 only!")

        if userInput == 1:
            userInput = input("Please Enter A Letter:")
            # These if statements checks if the letter picked is within the word.
            if num1 == 0:
                if userInput == "b" or "e" or "a" or "u" or "t" or "i" or "f" or "u" or "l":
                    if userInput == "b":
                        arrayCatcher9[0] = "b"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "e":
                        arrayCatcher9[1] = "e"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "a":
                        arrayCatcher9[2] = "a"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "u" and arrayCatcher9[3] !="u":
                        arrayCatcher9[3] = "u"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "t":
                        arrayCatcher9[4] = "t"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "i":
                        arrayCatcher9[5] = "i"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "f":
                        arrayCatcher9[6] = "f"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "u":
                        arrayCatcher9[7] = "u"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "l":
                        arrayCatcher9[8] = "l"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                if userInput != "b" and userInput != "e" and userInput != "a" and userInput != "u" and userInput != "t" and userInput != "i" and userInput != "f" and userInput != "l":
                    numGuess -= 1
                    print("Sorry you enter a wrong letter, you have " + str(numGuess) + " left over!")

            if num1 == 1:
                if userInput == "r" or "o" or "b" or "i" or "n" or "h" or "o" or "o" or "d":
                    if userInput == "r":
                        arrayCatcher9[0] = "r"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "o" and arrayCatcher9[1] !="o":
                        arrayCatcher9[1] = "o"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "b":
                        arrayCatcher9[2] = "b"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "i" and arrayCatcher9[3] !="i":
                        arrayCatcher9[3] = "i"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "n":
                        arrayCatcher9[4] = "n"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "h":
                        arrayCatcher9[5] = "h"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "o" and arrayCatcher9[6] !="o":
                        arrayCatcher9[6] = "o"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "o":
                        arrayCatcher9[7] = "o"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                    elif userInput == "d":
                        arrayCatcher9[8] = "d"
                        print("You have guessed right.")
                        print(arrayCatcher9)

                if userInput != "r" and userInput != "o" and userInput != "b" and userInput != "i" and userInput != "n" and userInput != "h" and userInput != "o" and userInput != "o" and userInput != "d":
                    numGuess -= 1
                    print("Sorry you enter a wrong letter, you have " + str(numGuess) + " left over!")

            if num1 == 2:
                if userInput == "c" or "e" or "n" or "s" or "o" or "r" or "s" or "h" or "i" or "p":
                    if userInput == "c":
                        arrayCatcher10[0] = "c"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "e":
                        arrayCatcher10[1] = "e"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "n":
                        arrayCatcher10[2] = "n"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "s" and arrayCatcher10[3] !="s":
                        arrayCatcher10[3] = "s"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "o":
                        arrayCatcher10[4] = "o"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "r":
                        arrayCatcher10[5] = "r"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "s":
                        arrayCatcher10[6] = "s"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "h":
                        arrayCatcher10[7] = "h"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "i":
                        arrayCatcher10[8] = "i"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                    elif userInput == "p":
                        arrayCatcher10[9] = "p"
                        print("You have guessed right.")
                        print(arrayCatcher10)

                if userInput != "c" and userInput != "e" and userInput != "n" and userInput != "s" and userInput != "o" and userInput != "r" and userInput != "h" and userInput != "i" and userInput != "p":
                    numGuess -= 1
                    print("Sorry you enter a wrong letter, you have " + str(numGuess) + " left over!")

            if num1 == 3:
                if userInput == "u" or "l" or "t" or "i" or "m" or "a" or "t" or "e":
                    if userInput == "u":
                        arrayCatcher8[0] = "u"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "l":
                        arrayCatcher8[1] = "l"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "t" and arrayCatcher8[2] != "t":
                        arrayCatcher8[2] = "t"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "i" and arrayCatcher9[3] != "i":
                        arrayCatcher8[3] = "i"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "m":
                        arrayCatcher8[4] = "m"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "a":
                        arrayCatcher8[5] = "a"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "t":
                        arrayCatcher8[6] = "t"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                    elif userInput == "e":
                        arrayCatcher8[7] = "e"
                        print("You have guessed right.")
                        print(arrayCatcher8)

                if userInput != "u" and userInput != "l" and userInput != "t" and userInput != "i" and userInput != "m" and userInput != "a" and userInput != "t" and userInput != "e":
                    numGuess -= 1
                    print("Sorry you enter a wrong letter, you have " + str(numGuess) + " left over!")


        elif userInput == 2:
            userInput = input("Guess the word correctly:")
            if userInput == hangmanList[num1] and numGuess > 0:
                print("You have guess the word correctly, You have won the game!...Thanks for playing..:)")
                quit()

            elif userInput != hangmanList[num1]:
                numGuess -= 1
                print("You have guessed wrong, you have:" + str(numGuess) + " guesses left over!")









