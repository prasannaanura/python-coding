import random

randomNumber = random.randint(1,10)

while True:
    guessNumber = int(input("Enter a number between 1 and 10 "))
    if randomNumber == guessNumber:
        print("you win!")
        break
    elif randomNumber > guessNumber:
        print("Your guess too high!")
    else:
        print("Your guess low!")
