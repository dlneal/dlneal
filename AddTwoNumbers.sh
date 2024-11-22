#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables

function add_numbers() {
local num1=$1
local num2=$1
echo "Addition: $num1 + $num2 = $((num1 + num2))"
}