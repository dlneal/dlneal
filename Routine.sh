#!/bin/bash

# Function to show the current time and date
show_date_time() {
    echo "Current date and time: $(date)"
}

# Function to create a quick note
create_note() {
    read -p "What do you want to note? " note
    echo "$note" >> quick_notes.txt
    echo "Your note has been saved to quick_notes.txt."
}

# Function to quickly check if the internet is working
check_internet() {
    echo "Checking internet connection..."
    if ping -c 1 google.com &>/dev/null; then
        echo "The internet is working!"
    else
        echo "No internet connection."
    fi
}

# Main menu
echo "What do you want to do?"
echo "1) Show the date and time"
echo "2) Write a quick note"
echo "3) Check if the internet is working"
echo "4) Quit"

read -p "Pick a number: " choice

case $choice in
    1)
        show_date_time
        ;;
    2)
        create_note
        ;;
    3)
        check_internet
        ;;
    4)
        echo "Goodbye!"
        ;;
    *)
        echo "That's not a valid choice. Bye!"
        ;;
esac
