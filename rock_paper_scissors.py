import random

options = ["rock", "paper", "scissors"]                                                                 # List of options for the computer to choose from
user_points = 0                                                                                         # User's score counter
comp_points = 0                                                                                         # Computer's score counter

while True:                                                                                             # Infinite loop to keep the game running                                          
    user_option = input("Choose 'rock', 'paper', or 'scissors'. Enter 'quit' to exit game: ").lower()   # Get user input and convert to lowercase

    if user_option not in options and user_option != "quit":                                            # Validate user input
        print("Invalid option. Please try again.")                                                      # Prompt user to try again if input is invalid
    else:
        if user_option == "quit":                                                                       # Check if user wants to quit the game                                 
            if user_points > comp_points:                                                               # Check who has more points to declare the winner
                print("You won the game!")
            else: 
                print("The computer won the game!")
            print(f"Your points: {user_points} | Computer points: {comp_points}")                        # Display final scores    
            break

        comp_option = random.choice(options)                                                             # Randomly select an option for the computer
        print(f"The computer chose: {comp_option}")                                                      # Display the computer's choice

        if user_option == comp_option:                                                                   # Check for a tie  
            print("It's a tie!")
        elif (user_option == "rock" and comp_option == "scissors") or \
            (user_option == "paper" and comp_option == "rock") or \
            (user_option == "scissors" and comp_option == "paper"):                                      # Check if user wins the round. If so, increment user's score by 1 and display user's total score
            user_points += 1
            print("You win this round! Your points:", user_points)
        else:                                                                                            # Else, the computer wins the round. In this case, increment the computer's score by 1 and display the computer's total score
            comp_points += 1
            print("The computer wins this round! Computer points:", comp_points)

