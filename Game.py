yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

# Say hello!
name = input("Hi! What's your name?\n")
print("Hello, " + name + "! Let's go on an adventure!")
print("You are standing at the edge of a big, dark forest.")
print("Can you find your way through?\n")

# Start the game
response = ""
while response not in yes_no:
    response = input("Do you want to go into the forest? Type yes or no.\n").lower()
    if response == "yes":
        print("Yay! You step into the forest. Birds are singing!\n")
    elif response == "no":
        print("Oh no! Maybe next time. Goodbye, " + name + "!")
        quit()
    else: 
        print("Oops! Try typing yes or no.\n")

# Pick a path
response = ""
while response not in directions:
    response = input("There are four ways to go! Do you go left, right, forward, or backward?\n").lower()
    if response == "left":
        print("Oh! There is a big river. A small boat is here.\n")
        boat = input("Do you get in the boat? yes or no?\n").lower()
        if boat == "yes":
            print("Hooray! You float across safely.\n")
        else:
            print("Uh-oh! You can’t cross and get lost. Game over.")
            quit()
    elif response == "right":
        print("Oh no! A big, scary wolf is here!\n")
        fight = input("Do you fight or run?\n").lower()
        if fight == "fight":
            print("Wow! You are so brave! You win and find a treasure chest!\n")
        else:
            print("Oh no! The wolf is too fast. Game over.")
            quit()
    elif response == "forward":
        print("Look! A little house is here. The door is open.\n")
        enter = input("Do you go inside? yes or no?\n").lower()
        if enter == "yes":
            print("Wow! A friendly wizard gives you a magic map. You win!")
        else:
            print("Oh no! It gets dark, and you get lost. Game over.")
            quit()
    elif response == "backward":
        print("Oops! The path behind you is gone! You are stuck. Game over.")
        quit()
    else:
        print("Oops! Try typing left, right, forward, or backward.\n")
