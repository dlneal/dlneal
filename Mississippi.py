# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:

import time  # This lets us make the program wait for a moment.

# Let's count to five!
for number in range(1, 6):  # This means: start at 1 and stop at 5.
    print(number, "Mississippi")  # Say the number and "Mississippi".
    time.sleep(1)  # Wait for 1 second.

# After counting, say the special message.
print("Ready or not, here I come!")
