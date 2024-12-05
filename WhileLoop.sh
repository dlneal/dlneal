#!/bin/bash

while true; do
    echo "Please choose an option:"
    echo "1: Echo 'Hello World'"
    echo "2: Ping a website or IP address"
    echo "3: Run ifconfig"
    echo "4: Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Hello World"
            ;;
        2)
            read -p "Enter a website or IP address to ping: " target
            if [[ -n $target ]]; then
                ping -c 4 "$target"
            else
                echo "No target entered."
            fi
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting. Goodbye!"
            break
            ;;
        *)
            echo "Invalid entry. Please try again."
            ;;
    esac

    echo # Add a blank line for readability
done


