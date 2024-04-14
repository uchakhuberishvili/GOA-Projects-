import random
while True:
    choice = ["rock","paper","scissors"]
    player = None
    computer = random.choice(choice)
    while player not in choice:
        player = input("rock,paper.scissors?: ").lower()
    if player == computer:
       print("computer: ",computer)
       print("player: ",player)
       print("Tie")
    elif player == "rock":
       if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You lose!")
       if computer == "scissors":
               print("computer: ",computer)
               print("player: ",player)
               print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
        if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose!")
    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
         break
print("Bye")
