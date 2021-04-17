#!/bin/bash

cd Desktop
touch to-do.txt

echo "Applying Easy Linux Tips' Recommended steps"

sudo chown -Rc $USER:$USER $HOME
chmod -f 700 $HOME
echo "Set proper permissions for $USER's home"

echo "- LibreOffice" >> to-do.txt
echo "  - Disable Java" >> to-do.txt
echo "    - LibreOffice Writer > Tools > Options > LibreOffice > Advanced > Java Options" >> to-do.txt
echo "    - Disable 'Use a Java runetime environment'" >> to-do.txt

echo "- Turn off some startup applications" >> to-do.txt
echo "  - Menu > Preferences > Startup Applications" >> to-do.txt
echo "  - Recommended:" >> to-do.txt
echo "    - System Reports" >> to-do.txt
echo "    - mintwelcome" >> to-do.txt
echo "    - Support for NVIDIA Prime" >> to-do.txt
echo "    - Warpinator" >> to-do.txt
echo "- Adjust Power Manager (Laptop Only)" >> to-do.txt
echo "  - Right click the battery icon on the panel" >> to-do.txt

echo "- Disable Mousepad while typing (Laptop Only)" >> to-do.txt
echo "  - Menu > Preferences > Mouse and Touchpad > Touchpad > General" >> to-do.txt
echo "    - Set 'Disable touchpad while typing' to OFF" >> to-do.txt

sudo apt-get install -q xserver-xorg-input-synaptics
sudo mkdir -q /etc/X11/xorg.conf.d 
sudo cp /usr/share/X11/xorg.conf.d/70-synaptics.conf /etc/X11/xorg.conf.d/70-synaptics.conf

echo "  - Menu > Preferences > Startup Applications > Add > Custom command" >> to-do.txt
echo "    - Name: Syndaemon" >> to-do.txt
echo "    - Command: syndaemon -i 1.0 -K -R -t" >> to-do.txt
echo "    - Comment: Disable the touchpad while typing, with a reasonable delay of one second and only for tapping and scrolling" >> to-do.txt
echo "    - Startup delay: 10 sec" >> to-do.txt

sudo apt-get install -q dconf-editor

echo "- Disable 'switch user'" >> to-do.txt
echo "  - dconf-editor > org > cinnamon > desktop > lockdown" >> to-do.txt
echo "  - set 'disable-user-switching' to ON" >> to-do.txt

sudo apt-get install -q numlockx

echo "- Turn Num Lock on automatically" >> to-do.txt
echo "  - Menu > Administration > Login Window > Settings > Activate numlock" >> to-do.txt

sudo apt-get remove -q gnome-orca
echo "Orca removed"

echo "- Get Weather applet" >> to-do.txt
echo "  - Right click panel > Applets > Download > Weather" >> to-do.txt
echo "  - Applets > Manage > Weather > +" >> to-do.txt