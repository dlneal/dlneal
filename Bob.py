# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random

def guessing_game():
    while True:
        number_to_guess = random.randint(1, 20)
        print("\nGuess a number between 1 and 20!")
        attempts = 0

        while True:
            try:
                guess = int(input("Your guess: "))
                if not 1 <= guess <= 20:
                    print("Pick a number between 1 and 20.")
                    continue
            except ValueError:
                print("That's not a number. Try again!")
                continue

            attempts += 1
            if guess < number_to_guess:
                print("Go higher!")
            elif guess > number_to_guess:
                print("Go lower!")
            else:
                print(f"You got it in {attempts} tries!")
                break

        if input("Play again? (yes/no): ").strip().lower() != "yes":
            print("Thanks for playing! Bye!")
            break

if __name__ == "__main__":
    guessing_game()
