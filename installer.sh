#!/bin/bash
wget https://raw.githubusercontent.com/Briiqn/TuxClicker/main/dependencies.txt && pip install -r dependencies.txt && clear
echo done installing dependencies, downloading tuxclicker
clear
wget https://github.com/Briiqn/TuxClicker/releases/download/Release5/tuxclicker-nuitka
wget https://github.com/Briiqn/TuxClicker/raw/main/ristretto
clear
sudo cp ristretto /usr/bin/
echo download done
echo starting...
chmod ugo+rwx tuxclicker-nuitka
echo done!!
./tuxclicker-nuitka

