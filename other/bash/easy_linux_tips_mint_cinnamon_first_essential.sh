#!/bin/bash

# Apply all available updates
echo Welcome!
echo Applying Easy Linux Tips\' \"10 Things to Do First in Linux Mint 20.1 Cinnamon\"
sudo apt-get update -q
sudo apt-get upgrade -q
echo Software updated!
cd Desktop
touch to-do.txt
echo "- Configure Timeshift" >> to-do.txt
echo "- Update Manager" >> to-do.txt 
echo "  - Select local mirror" >> to-do.txt 
echo "  - Set automatic cleaning" >> to-do.txt to select a local mirror, and to automatically clean.

# Install some useful tools and an extra media player
sudo apt-get install doublecmd-gtk -q
sudo apt-get install pavucontrol -q
sudo apt-get install rar -q
sudo apt-get install p7zip-rar -q
sudo apt-get install catfish -q
sudo apt-get install vlc -q
echo "Utilities installed!"

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

echo "- LibreOffice" >> to-do.txt
echo "  - Configure fonts:" >> to-do.txt
echo "    - LibreOffice Writer > Tools > Options > LibreOffice > Fonts" >> to-do.txt
echo "    - Check 'Apply replacement table'" >> to-do.txt
echo "    - Add 'Calibri' -> 'Carlito'" >> to-do.txt
echo "    - Add 'Cambria' -> 'Caladea'" >> to-do.txt
echo "    - Check 'Always' and 'Screen only' for both" >> to-do.txt

echo "Reboot to apply all changes" >> to-do.txt