#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/

#!/bin/bash
# A simple script to ask about your day

echo "How is your day? (good/bad)"
read answer

case $answer in
    good)
        echo "Yay! I'm happy you're having a good day!"
        ;;
    bad)
        echo "Oh no! I hope your day gets better soon."
        ;;
    *)
        echo "Hmm, I don't understand. Please say 'good' or 'bad'."
        ;;
esac
