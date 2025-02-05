# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:

import random

choices = ['rock', 'paper', 'scissors']

while True:
    user = input("rock, paper, scissors? (or 'quit' to stop): ").lower()
    if user == 'quit':
        print("Bye!")
        break
    if user not in choices:
        print("Try again!")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
        (user == 'paper' and computer == 'rock') or \
        (user == 'scissors' and computer == 'paper'):
        print("You win!")
    else:
        print("You lose!")
    
    print()
    
