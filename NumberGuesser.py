# create number guessing game where person guesses number between 1 and 10, person will get hints and after
# three guesses will be given the answer

print("Hello and welcome to the number guessing game, you will get three guesses and will get a hint after the first" \
      " two guesses, after the third guess you will be given the number")

guess = int(input("Please enter a number between 1 and 10   "))

print("Your guess is  " + str(guess))

import random

number = random.randint(1, 10)

if guess == number:
    print("You win")
elif guess < number:
    print("Your guess is low")
else:
    print ("Your guess is to high")

if guess != number:
    guess = int(input("Please enter a number between 1 and 10   "))

    print("Your guess is  " + str(guess))

    if guess == number:
        print("You win")
    elif guess < number:
        print("Your guess is low")
    else:
        print ("Your guess is to high")

if guess != number:
    guess = int(input("Please enter a number between 1 and 10   "))

    print("Your guess is  " + str(guess))

    if guess == number:
        print ("You Win!")
    else:
        print("Better luck next time!")
