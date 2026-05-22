#!/bin/bash

# Download gets the rest of the github repo
    echo "Downloading the rest of the repo..."
    git clone https://github.com/Wm-Mason-Cyber/oled-ip-display-for-rpi
#runs normal install script
    bash ~/oled-ip-display-for-rpi/install.sh
#runs the ip.py automatically
    python3 ~/oled-ip-display-for-rpi/ip.py &
