#!/bin/bash

# Challenge today is to create a script that list all the devices on the network and ask the user to ping one of the ip address.
# There is a few different ways to list all deivices on your network you could use an arp command or an nmap command.
# We will run the a command that prints all address then ask the user to ping a specific one by entering an ip address.

#!/bin/bash

# List devices on the network
list_devices() {
echo "Scanning the network..."

if command -v nmap &>/dev/null; then
    nmap -sn 192.168.1.0/24 | awk '/Nmap scan report/{print $5}' > devices.txt
else
    arp -a | awk '{print $2}' | tr -d '()' > devices.txt
fi

if [[ -s devices.txt ]]; then
    echo "Devices found:"
    nl devices.txt
else
    echo "No devices found. Exiting."
    exit 1
fi
}

# Ping a selected IP address
ping_device() {
echo "Select a device to ping (number):"
read -r selection

ip=$(sed -n "${selection}p" devices.txt)

if [[ -z $ip ]]; then
    echo "Invalid choice. Exiting."
    exit 1
fi

ping -c 4 "$ip"
}

list_devices
ping_device
