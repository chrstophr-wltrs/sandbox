#!/bin/bash

# Apply all available updates
echo Welcome!
echo Applying Easy Linux Tips\' \"10 Things to Do First in Linux Mint 20.1 Cinnamon\"
sudo apt-get update -q
sudo apt-get upgrade -q
echo Software updated! 
echo Remember to configure Timeshift!
echo You should adjust Update Manager to select a local mirror, and to automatically clean.

# Install some useful tools and an extra media player
sudo apt-get install doublecmd-gtk -q
sudo apt-get install pavucontrol -q
sudo apt-get install rar -q
sudo apt-get install p7zip-rar -q
sudo apt-get install catfish -q
sudo apt-get install vlc -q
echo Utilities installed!

# Decrease the swap use
sudo echo "vm.swappiness = 10" >> /etc/sysctl.conf
echo "Adjusted swappiness to 10"

# Turn on the firewall
sudo ufw enable
sudo ufw logging off
echo "Firewall enabled!"

# Improve font support
wget http://ftp.us.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-installer_3.8_all.deb -P ~/Downloads
sudo apt-get install ~/Downloads/ttf-mscorefonts-installer_3.8_all.deb -q
rm -f ~/Downloads/ttf-mscorefonts-installer_3.8_all.deb
sudo dpkg-reconfigure fontconfig
sudo apt-get install fonts-crosextra-carlito fonts-crosextra-caladea -q
echo "Microsoft compatibility fonts installed!"
echo "Remember to configure the replacement fonts in LibreOffice:"
echo "LibreOffice Writer > Tools > Options > LibreOffice > Fonts"
echo "Check 'Apply replacement table'"
echo "Add 'Calibri' -> 'Carlito'"
echo "Add 'Cambria' -> 'Caladea'"
echo "Check 'Always' and 'Screen only' for both"