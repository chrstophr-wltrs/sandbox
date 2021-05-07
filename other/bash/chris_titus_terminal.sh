#!/bin/bash

echo "Applying Chris Titus Tech terminal settings"

# Get terminator
sudo apt-get update -q
sudo apt-get install -q terminator
echo "Terminator installed"

# Get zsh
sudo apt-get install -q zsh zsh-syntax-highlighting autojump zsh-autosuggestions
echo "zsh and associated packages installed"

# Initial setup
touch "$HOME/.cache/zshhistory"
#-- Setup Alias in $HOME/zsh/aliasrc
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
cd ~
wget -q https://raw.githubusercontent.com/ChrisTitusTech/zsh/master/.zshrc

# Install fonts
cd /usr/share/fonts/truetype/
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf
sudo wget -q https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf
echo "Meslo Fonts installed"

# Preference Changes should really be done in the GUI
cd ~/Desktop
touch to-do.txt
echo "- Use Terminator as default terminal" >> to-do.txt
echo "  - Menu > Preferences > Preferred Applications > Terminal" >> to-do.txt
echo "- Terminator preferences" >> to-do.txt
echo "  - Use system font -> OFF" >> to-do.txt
echo "    - Switch font to 'MesloGS NF Regular'" >> to-do.txt
echo "    - Do the same thing in Profiles > default > General" >> to-do.txt
echo "  - Enable background transparency" >> to-do.txt
echo "    - Profiles > default > Background" >> to-do.txt

# Change default shell to zsh
echo "Use '/bin/zsh' when prompted"
chsh $USER
echo "Now close down and restart the terminal"
echo "Use 'p10k configure' if nothing happens"