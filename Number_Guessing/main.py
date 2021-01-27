import random

# Just a simple game where the user input a number and has to guess right. Only three attempts.
class Play:
    num = random.randint(1,10)
    print("The answer is: " + str(num))
    userInput = int(input("Please Guess A Number From 1 to 10, You Have Three Attempts:"))
    attempts = 0
    while attempts < 3:
        attempts += 1
        if userInput == num:
            print("Congratulations, You Have Enter The Right Number. You Won The Game!")
            break
        elif attempts == 3:
            print("Sorry You Used All Your Attempts, Game Over!")
            break
        elif userInput > num:
            print("The attempts are:" + str(attempts))
            userInput = int(input("You Have Guess Wrong, Please Guess Lower:"))
        elif userInput < num:
            print("The attempts are:" + str(attempts))
            userInput = int(input("You Have Guess Wrong, Please Guess Higher:"))




