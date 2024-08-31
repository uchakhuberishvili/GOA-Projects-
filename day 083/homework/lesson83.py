import random

print("Welcome to Rock, Paper, Scissors!")

user_choice = input("Enter rock, paper, or scissors: ").lower()

while user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please try again.")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)


print(f"You chose {user_choice}.")
print(f"The computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("You lose!")
