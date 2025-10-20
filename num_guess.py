import random

comp_num = random.randint(1, 100)                                                               # Generate a random number between 1 and 100

def lives(counter):                                                                             # lives function has counter parameter for the number of tries based on difficulty level
    inf_counter = 0                                                                             # inf_counter tracks number of tries, good for the unlimited tries mode
    while counter > 0:                                                                          # counter tracks number of tries for easy, hard, unlimited tries modes 
        user_option = input("Guess a number between 1 and 100 OR enter 0 to exit game: ")       # Get user input
        if user_option.isdigit() and (1 <= int(user_option) <= 100 or int(user_option) == 0):   # Check if user input is a digit and within valid range 
            counter -= 1                                                                        # Decrement counter by 1 each time user makes a guess                           
            inf_counter += 1                                                                    # Increment inf_counter by 1 each time user makes a guess
            user_num = int(user_option)                                                         # Convert user input to integer
            if user_num == 0:                                                                   # Check if user wants to quit the game
                break
            elif user_num < comp_num:                                                           # Check if user's guess is too low
                print("Too low")
            elif user_num > comp_num:                                                           # Check if user's guess is too high
                print("Too high")
            elif user_num == comp_num:                                                          # Check if user's guess is correct
                print("Correct! You guessed the number in", inf_counter, "tries.")
                break
        else:
            print("Invalid number. Please try again.")                                          # Invalid user input, prompt user to try again
    print("Gamer over! The correct number was", comp_num)                                       # Display game over message with the correct number, good for when user fails to guess correct number with limited tries


while True:
    user_level = input("Choose a difficulty level 'easy', 'hard', 'unlimited tries' OR enter 0 to exit game: ").lower() # Get user input for difficulty level and convert to lowercase

    # Call lives function with appropriate number of tries based on difficulty level (easy - 10 tries, hard - 5 tries, unlimited tries - infinite tries)
    if user_level in ["easy", "hard", "unlimited tries", "0"]:
        if user_level == "0":                                                                   # Check if user wants to quit the game
            break
        if user_level == "easy":                                                                                                
            lives(10)
        elif user_level == "hard":
            lives(5)
        elif user_level == "unlimited tries":
            lives(float('inf'))
    else:
        print("Invalid difficulty level. Please try again.")  # Invalid user input, prompt user to try again
        