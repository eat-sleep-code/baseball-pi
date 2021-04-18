# Baseball Pi

How did the old 1970's Chevy jingle go?  *"**Baseball**, hot dogs, **apple pie** and Chevrolet, they go together in the good ol’ USA."*   Well what about **baseball** and **RASPBERRY PI**?   

Get the live box score, plays, and batter stats of your favorite MLB team[\*](#important-notice) right on your desktop.

:baseball: [View images and a short video of this device.](https://eat-sleep-code.com/blog/get-the-live-box-score-plays-and-batter-stats-of-your-favorite-mlb-team-right-on-your-desktop)

## Hardware Requirements
* [Raspberry Pi Zero W](https://www.adafruit.com/product/3400)
* [GPIO Male Headers](https://www.adafruit.com/product/3413)
* [Pi Supply PaPiRus Zero ePaper/eInk pHAT v1.2](https://www.adafruit.com/product/3335)

___

---
## Getting Started

- Use [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) to:
  - Set the Memory Split value to a value of 16MB
  - Set up your WiFi connection
- Connect the Raspberry Pi HQ Camera to your Raspberry Pi

* Run `sudo nano /etc/apt/sources.list`[\*\*](https://www.nano-editor.org/dist/v2.8/nano.html) and uncomment the reference to the source repo 

___

## Installation
* Installation of the program, any software prerequisites, as well as the e-ink display drivers can be completed with the following two-line install script.

```
wget -q https://raw.githubusercontent.com/eat-sleep-code/baseball-pi/master/install-baseball.sh -O ~/install-baseball.sh
sudo chmod +x ~/install-baseball.sh && ~/install-baseball.sh

```

___

## Usage Example ##

```
baseball --team Orioles
```
___

## Options ##

Options
* --team : Set the MLB team name (default: D-backs)
* --refresh : Set the refresh rate in seconds (default: 15)

## Autorun ##

Want to start Baseball Pi every time you boot your Raspberry Pi?  Here is how!
* Run `sudo nano /etc/systemd/system/baseball.service`[\*\*](https://www.nano-editor.org/dist/v2.8/nano.html) and enter the following lines (be sure to specify your favorite team!): 
````
[Unit]
Description=Baseball Pi service

[Service]
ExecStart=/usr/bin/python3 /home/pi/baseball/baseball.py --team Orioles
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=Baseball Pi
User=pi

[Install]
WantedBy=multi-user.target
````
* Run `sudo systemctl enable baseball.service`
* Run `sudo systemctl start baseball.service`
* Run `sudo reboot`

___
___

### IMPORTANT NOTICE ###
All game data is the property of Major League Baseball Properties, Inc.    This code was created for personal use only and does not construe any rights to use this data without the express permission of Major League Baseball Properties, Inc.   Other trademarks used throughout this repository are the property of their respective owners and are used for identification purposes only.   You may not hold the owners and operators (or any associated parties) of the \<eat-sleep-code /\> websites and repositories liable or financially responsible for any damages including—but not limited to—emotional, physical, or financial damages incurred during or after the use of this repository or any referenced websites. Use of this repository and/or the code found within constitutes an agreement to these terms.







