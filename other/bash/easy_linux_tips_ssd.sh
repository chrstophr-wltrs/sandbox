#!/bin/bash

sudo mkdir /etc/systemd/system/fstrim.timer.d
sudo touch /etc/systemd/system/fstrim.timer.d/override.conf
sudo echo "[Timer]" >> /etc/systemd/system/fstrim.timer.d/override.conf
sudo echo "OnCalendar=" >> /etc/systemd/system/fstrim.timer.d/override.conf
sudo echo "OnCalendar=daily" >> /etc/systemd/system/fstrim.timer.d/override.conf