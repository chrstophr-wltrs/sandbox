#!/bin/bash

# Apply all available updates
echo Welcome!
echo Applying Easy Linux Tips\' \"10 Things to Do First in Linux Mint 20.1 Cinnamon\"
cd Desktop
touch to-do.txt
echo "- Configure Timeshift" >> to-do.txt
echo "  - 2x a month" >> to-do.txt
echo "- Update Manager" >> to-do.txt 
echo "  - Select local mirror" >> to-do.txt 
echo "  - Set automatic cleaning" >> to-do.txt to select a local mirror, and to automatically clean.

# Install some useful tools and an extra media player
sudo apt-get install -q doublecmd-gtk   
sudo apt-get install -q pavucontrol
sudo apt-get install -q rar
sudo apt-get install -q p7zip-rar
sudo apt-get install -q catfish
sudo apt-get install -q vlc
echo "Utilities installed!"

# Decrease the swap use
sudo echo "vm.swappiness = 10" >> /etc/sysctl.conf
echo "Adjusted swappiness to 10"

# Turn on the firewall
sudo ufw enable
sudo ufw logging off

# Improve font support
wget http://ftp.us.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-installer_3.8_all.deb -P ~/Downloads
sudo apt-get install -q ~/Downloads/ttf-mscorefonts-installer_3.8_all.deb
rm -f ~/Downloads/ttf-mscorefonts-installer*.deb
sudo dpkg-reconfigure -u fontconfig
sudo apt-get install -q fonts-crosextra-carlito fonts-crosextra-caladea
echo "Microsoft compatibility fonts installed!"

echo "- LibreOffice" >> to-do.txt
echo "  - Configure fonts:" >> to-do.txt
echo "    - LibreOffice Writer > Tools > Options > LibreOffice > Fonts" >> to-do.txt
echo "    - Check 'Apply replacement table'" >> to-do.txt
echo "    - Add 'Calibri' -> 'Carlito'" >> to-do.txt
echo "    - Add 'Cambria' -> 'Caladea'" >> to-do.txt
echo "    - Check 'Always' and 'Screen only' for both" >> to-do.txt
