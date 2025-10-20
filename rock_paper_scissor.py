import random

options = ["rock", "paper", "scissors"]
user_points = 0
comp_points = 0

while True:
    user_option = input("Choose 'rock', 'paper', or 'scissors'. Enter 'quit' to exit game: ").lower()

    if user_option == "quit":
        if user_points > comp_points:
            print("You won the game!")
            print(f"Your points: {user_points} | Computer points: {comp_points}")
        else: 
            print("The computer won the game!")
            print(f"Your points: {user_points} | Computer points: {comp_points}")
        break

    comp_option = random.choice(options)
    print(f"The computer chose: {comp_option}")

    if user_option == comp_option:
        print("It's a tie!")
    elif (user_option == "rock" and comp_option == "scissors") or \
         (user_option == "paper" and comp_option == "rock") or \
         (user_option == "scissors" and comp_option == "paper"):
        user_points += 1
        print("You win this round! Your points:", user_points)
    else:
        comp_points += 1
        print("The computer wins this round! Computer points:", comp_points)

