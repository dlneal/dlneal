# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Import the random module so we can pick something randomly
import random

# Ask the user to type everyone's names, separated by commas
names_string = input("Enter everyone's names, separated by a comma: ")

# Turn the list of names into a list (split at each comma)
names = names_string.split(", ")

# Pick one random name from the list
random_person = random.choice(names)

# Print the name of the person who will pay
print(random_person + " will pay for everyone's food!")

