# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Ask how old you are
age = int(input("How old are you? "))

# You can live up to 90 years
years_left = 90 - age

# Figure out the time left
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# Tell you how much time is left
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to live!")
