# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

import requests

# Ask for the website
url = input("Enter a website URL: ")

# Ask for the type of request
print("Choose a request type: 1 = GET, 2 = POST, 3 = PUT, 4 = DELETE")
choice = input("Enter the number of your choice: ")

# Match the number to a request type
methods = {"1": "GET", "2": "POST", "3": "PUT", "4": "DELETE"}
method = methods.get(choice)
if not method:
    print("Invalid choice.")
    exit()

# Confirm and proceed
print(f"You chose {method} for {url}.")
if input("Type 'yes' to continue: ").lower() != "yes":
    print("Canceled.")
    exit()

# Perform the request
try:
    response = requests.request(method, url)
    print(f"Response Code: {response.status_code}")
    if response.status_code == 404:
        print("Site not found.")
    elif response.status_code == 200:
        print("Success!")
    else:
        print("Something happened.")
except Exception as e:
    print(f"Error: {e}")
