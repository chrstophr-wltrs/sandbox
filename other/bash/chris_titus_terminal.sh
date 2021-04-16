#!/bin/bash

# Get terminator
sudo apt-get update -q
sudo apt-get install -q terminator

# Get zsh
sudo apt-get install -q zsh zsh-syntax-highlighting autojump zsh-autosuggestions

# Initial setup
touch "$HOME/.cache/zshhistory"
#-- Setup Alias in $HOME/zsh/aliasrc
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc

# Install fonts
cd /usr/share/fonts/truetype/
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf

# Preference Changes should really be done in the GUI
cd ~/Desktop
touch to-do.txt
echo "- Terminator preferences" >> to-do.txt
echo "  - Use system font -> OFF" >> to-do.txt
echo "    - Switch font to 'MesloGS NF Regular'" >> to-do.txt
echo "    - Do the same thing in Profiles > default > General" >> to-do.txt
echo "  - Enable background transparency" >> to-do.txt
echo "    - Profiles > default > Background" >> to-do.txt