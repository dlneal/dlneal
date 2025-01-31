# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Ask for the total bill amount
bill = float(input("How much is the total bill? $"))

# Ask for the number of people
people = int(input("How many people are sharing the bill? "))

# Ask for the tip percentage
tip_percentage = float(input("What tip percentage do you want to add? "))

# Add the tip to the bill
total_bill = bill + (bill * tip_percentage / 100)

# Split the bill among everyone
share = total_bill / people

# Round the amount to 2 decimal places
share = round(share, 2)

# Show how much each person should pay
print(f"Each person pays: ${share:.2f}")
