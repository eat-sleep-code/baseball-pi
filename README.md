# Baseball Pi

How did the old 1970's Chevy jingle go?  *"**Baseball**, hot dogs, **apple pie** and Chevrolet, they go together in the good ol’ USA."*   Well what about **baseball** and **RASPBERRY PI**?   

Get the live box score, plays, and batter stats of your favorite MLB team[\*](#important-notice) right on your desktop.

:baseball: [View images and a short video of this device.](https://eat-sleep-code.com/blog/get-the-live-box-score-plays-and-batter-stats-of-your-favorite-mlb-team-right-on-your-desktop)

## Hardware Requirements
* [Raspberry Pi Zero W](https://www.adafruit.com/product/3400)
* [GPIO Male Headers](https://www.adafruit.com/product/3413)
* [Pi Supply PaPiRus Zero ePaper/eInk pHAT v1.2](https://www.adafruit.com/product/3335)

___

## Software Requirements
### Configure your Pi ###
* Follow the [installation guide](https://www.raspberrypi.org/downloads/raspbian/) to download and install the latest build of **Raspbian Jessie Lite**.
* Run `sudo raspi-config` and complete the following tasks:
  * Expand file system
  * Setup locale
  * Setup timezone
  * Setup keyboard
  * Set GPU memory to 16MB to allocate most memory to CPU
  * Set up WiFi using this [configuration guide](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
* Run `sudo nano /etc/apt/sources.list`[\*\*](https://www.nano-editor.org/dist/v2.8/nano.html) and uncomment the reference to the source repo 
* Run `sudo apt-get update`
* Run `sudo apt-get dist-upgrade`
* Run `sudo apt-get upgrade`
* **OPTIONAL:** If using macOS, run the following to allow easy copying of files to your Raspberry Pi: `sudo apt-get install netatalk`
___

### Installing the prerequisites ###
* Install Python and XML libraries
  * Run `sudo apt-get install python3 ipython3 ipython python3-pip python-pip python3-rpi.gpio python-rpi.gpio libxml2-dev libxslt-dev python-dev python3-lxml python-lxml`
  * Run `sudo apt-get build-dep python3-lxml`
* Install the LXML and Natural packages:
  * Run `sudo pip install lxml`
  * Run `sudo pip install natural`
* Setup PaPiRus screen
  * Run `curl -sSL https://pisupp.ly/papiruscode | sudo bash`

___

### Git and run ###
* Run `sudo git clone https://github.com/eat-sleep-code/baseball-pi`
* Run `python baseball/baseball.py --team [MLB Team]`   _for example: `python baseball/baseball.py --team Orioles`_

___

### Autorun ###
Want to start Baseball Pi every time you boot your Raspberry Pi?  Here is how!
* Run `sudo crontab -e`
* Select `nano`[\*\*](https://www.nano-editor.org/dist/v2.8/nano.html)
* Scroll to the bottom of the file and add these two lines:
    * `@reboot python baseball/baseball.py --team Orioles &`
    * `0 1 * * * python baseball/baseball.py --team Orioles &`
___

## Known Issues
See issues list[https://github.com/eat-sleep-code/baseball-pi/issues].

___
___

### IMPORTANT NOTICE ###
All game data is the property of Major League Baseball Properties, Inc.    This code was created for personal use only and does not construe any rights to use this data without the express permission of Major League Baseball Properties, Inc.   Other trademarks used throughout this repository are the property of their respective owners and are used for identification purposes only.   You may not hold the owners and operators (or any associated parties) of the \<eat-sleep-code /\> websites and repositories liable or financially responsible for any damages including—but not limited to—emotional, physical, or financial damages incurred during or after the use of this repository or any referenced websites. Use of this repository and/or the code found within constitutes an agreement to these terms.







