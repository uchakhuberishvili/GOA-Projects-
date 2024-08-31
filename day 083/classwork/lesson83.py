import random

number_to_guess = random.randint(1, 10)


print("I'm thinking of a number between 1 and 10.")
user_guess = int(input("Take a guess: "))


if user_guess == number_to_guess:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, that's not correct. The number was {number_to_guess}.")
