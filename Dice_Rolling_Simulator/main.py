#It will generate a random number and the user can play again and again to get a number from the dice
# until the user decides to quit the program
import random

class Play():
    userInput = input("Dice Rolling Simulator.. Press any key to continue..")
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    print("You rolled " + str(num1) + " and " + str(num2))


