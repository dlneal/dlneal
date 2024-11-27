#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.

run_domain_analysis () {
    echo "enter a domain name (e.g., google.com):"
    read domain

    output_file="domain_info.txt"

    echo "Running whois..." > "$output_file"
    whois "$domain" >> "$output_file" 2>&1
    echo -e "\nRunning dig..." >> "$output_file"
    dig "$domain" >> "$output_file" 2>&1
    echo -e "\nRunning host..." >> "$output_file"
    host "$domain" >> "$output_file" 2>&1
    echo -e "\nRunning nslookup..." >> "$output_file"
    nslookup "$domain" >> "$output_file" 2>&1

    echo "Results saved to $output_file"

    mousepad "$output_file"
}

while true; do
    echo "Select an option:"
    echo "1) Run whois"
    echo "2) run dig"
    echo "3) Run host"
    echo "4) Run nslookup"
    echo "5) Exit"
    echo "6) Domain analysis (whois, dig, host, nslookup)"

    read -p "Enter your choice: " choice

    case $choice in
        1) echo "Enter the domain name:"; -r domain; whois "$domain" ;;
        2) echo "Enter the domain name:"; -r domain; dig "$domain" ;;
        3) echo "Enter the domain name:"; -r domain; host "$domain" ;;
        4) echo "Enter the domain name:"; -r domain; nslookup "$domain" ;;
        5) echo "Exiting..."; exit 0 ;;
        6) run_domain_analysis ;;
        *) echo "Invalid option. Please tr again." ;;
    esac
done