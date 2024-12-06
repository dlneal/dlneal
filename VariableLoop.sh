#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is

# Initialize the variable
number=1

# Loop until the number is greater than 10
until [ "$number" -gt 10 ]; do
    echo "The curent number is: $number"
    ((number++))
done
