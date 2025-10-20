import random

comp_num = random.randint(1, 100)

def lives(counter):
    inf_counter = 0
    while counter > 0:
        user_num = int(input("Guess a number between 1 and 100 OR enter 0 to exit game: "))
        counter -= 1
        inf_counter += 1

        if user_num == 0:
            break
        elif user_num < comp_num:
            print("Too low")
        elif user_num > comp_num:
            print("Too high")
        elif user_num == comp_num:
            print("Correct! You guessed the number in", inf_counter, "tries.")
            break
    print("Gamer over! The correct number was", comp_num)


user_level = input("Choose a difficulty level 'easy', 'hard', 'unlimited tries': ").lower()

if user_level == "easy":
    lives(10)
elif user_level == "hard":
    lives(5)
elif user_level == "unlimited tries":
    lives(float('inf'))
    