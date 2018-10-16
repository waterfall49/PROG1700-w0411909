
import random
num_to_guess = random.randint(1,10)
current_guess = -1

while (num_to_guess != current_guess):
    current_guess = (input("Guess again (1-10): "))
    if not current_guess.isnumeric():
        print("Bad :(")
    elif int(current_guess) > num_to_guess:
        print("That was too high")
    elif int(current_guess) < num_to_guess:
        print("That was too low")
    else: 
        print("You got it!")
        break
