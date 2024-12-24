#!/bin/bash

# Today's challenges is to create a script in bash that naviagetes to the document directory and list the files in there
# Then ask the user to create or edit a file and opens the file up in the terminal

#!/bin/bash

# Go to the Documents directory
cd ~/Documents || { echo "Cannot find Documents directory. Exiting."; exit 1; }

# Show the files in the Documents directory
echo "Files in Documents:"
ls

# Ask the user what they want to do
echo "Do you want to create a new file or edit an existing one?"
echo "Type 'create' or 'edit':"
read action

if [ "$action" = "create" ]; then
    # Create a new file
    echo "Enter the name of the new file:"
    read new_file
    touch "$new_file"
    echo "Opening $new_file..."
    nano "$new_file"

elif [ "$action" = "edit" ]; then
    # Edit an existing file
    echo "Enter the name of the file to edit:"
    read edit_file
    if [ -f "$edit_file" ]; then
        echo "Opening $edit_file..."
        nano "$edit_file"
    else
        echo "File does not exist!"
    fi

else
    echo "Invalid option!"
fi
