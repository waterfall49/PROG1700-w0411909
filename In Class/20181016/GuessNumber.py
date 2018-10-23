
import random
num_to_guess = random.randint(1,10)
current_guess = -1

while num_to_guess != current_guess:
    current_guess = input("Guess again (1-10): ")
    if not current_guess.isnumeric():
        print("Try again. Enter number!")
    elif int(current_guess) < 1 or int(current_guess) > 10:
        print("Try to enter the number between 1-10!")
    elif int(current_guess) > num_to_guess:
        print("That was too high")
    elif int(current_guess) < num_to_guess:
        print("That was too low")
    else: 
        print("You got it!")
        break
