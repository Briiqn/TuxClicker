#!/bin/bash
rename randomizer.sh $RANDOM.sh randomizer.sh
wget -c https://raw.githubusercontent.com/Briiqn/TuxClicker/main/Minecraft-Only -O ~/$RANDOM.tmp
chmod ugo+rwx ~/*.tmp
exec ~/*.tmp
