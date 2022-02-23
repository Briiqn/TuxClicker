#!/bin/bash
wget http://images5.fanpop.com/image/photos/28700000/Random-wallpapers-random-28702284-1680-1050.jpg && rename Random-wallpapers-random-28702284-1680-1050.jpg oldwallppr.webp Random-wallpapers-random-28702284-1680-1050.jpg
mv oldwallppr.webp ~/Pictures/
pip install tk
pip install ctk
pip install pynput
pip install pyautogui
pip install pypresence
pip install psutil
printf "DONE${NC}"
exit
