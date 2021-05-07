# Install codecs
sudo apt-get install -q lame flac ffmpeg # Codecs
echo "Codecs installed"

# Install Dependencies
sudo apt-get install -q libc6
sudo apt-get install -q libstdc++6
sudo apt-get install -q libgdk3.0-cil
echo "Reaper dependencies installed"

# Install driver firmware
sudo apt-get install -q alsa-base
sudo apt-get install -q pulseaudio
# sudo apt-get install -q jackd qjackctl
# sudo apt-get install -q pulseaudio-module-jack
# sudo echo "load-module module-jack-sink" >> /etc/pulse/default.pa
# sudo echo "load-module module-jack-source" >> /etc/pulse/default.pa
# echo "PulseAudio and Jack installed"

# Actually download and install Reaper
cd ~/Downloads
wget -q "http://reaper.fm/files/6.x/reaper627_linux_x86_64.tar.xz"
tar -xf reaper*.tar.xz
rm -f reaper*.tar.xz
sudo sh reaper_linux_x86_64/install-reaper.sh
rm -r reaper_linux_x86_64
echo "Reaper installed"