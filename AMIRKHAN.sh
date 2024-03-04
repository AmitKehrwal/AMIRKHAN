#!/bin/bash

# Install Python packages
pip install pyppeteer==1.0.2
pip install pyppeteer_stealth
pip install getindianname
apt install wget -y
pip install webdriver_manager
pip install --upgrade webdriver_manager
apt install curl -y
curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
apt update -y
apt install brave-browser -y
