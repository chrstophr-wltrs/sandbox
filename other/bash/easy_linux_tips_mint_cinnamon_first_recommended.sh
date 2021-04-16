#!/bin/bash

cd Desktop
touch to-do.txt

sudo chown -Rc $USER:$USER $HOME

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