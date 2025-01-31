# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# You will need to use a for loop to write this:


#Write your code below this row 👇

for number in range(1, 101):  # Count from 1 to 100
    if number % 3 == 0 and number % 5 == 0:  # If it’s a FizzBuzz number
        print("FizzBuzz")
    elif number % 3 == 0:  # If it’s a Fizz number
        print("Fizz")
    elif number % 5 == 0:  # If it’s a Buzz number
        print("Buzz")
    else:  # If it’s just a regular number
        print(number)
