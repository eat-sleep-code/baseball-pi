# baseball-pi

How did the old 1970's Chevy jingle go?  *"Baseball, hot dogs, apple pie and Chevrolet, they go together in the good ol’ USA."*   Well what about Baseball and RASBERRY PI?   

Get the live box score, plays, and batter stats of your favorite MLB team right on your desktop:

## Hardware Requirements
* [Raspberry Pi Zero W](https://www.adafruit.com/product/3400)
* [GPIO Male Headers](https://www.adafruit.com/product/3413)
* [Pi Supply PaPiRus Zero ePaper/eInk pHAT v1.2](https://www.adafruit.com/product/3335)

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
* Run `sudo nano /etc/apt/sources.list` and uncomment the reference to the source repo
* Run `sudo apt-get update`
* Run `sudo apt-get dist-upgrade`
* Run `sudo apt-get upgrade`
* **OPTIONAL:** If using macOS, run the following to allow easy copying of files to your Raspberry Pi: `sudo apt-get install netatalk`

### Installing the prerequisites ###
* Install Python and XML libraries
  * Run `sudo apt-get install python3 ipython3 ipython python3-pip python-pip python3-rpi.gpio python-rpi.gpio libxml2-dev libxslt-dev python-dev python3-lxml python-lxml`
  * Run `sudo apt-get build-dep python3-lxml`
* Install the LXML and Natural packages:
  * Run `sudo pip install lxml`
  * Run `sudo pip install natural`
* Setup PaPiRus screen
  * Run `curl -sSL https://pisupp.ly/papiruscode | sudo bash`

### Git and run ###
* Run `sudo git clone https://github.com/eat-sleep-code/baseball-pi`
* Run `baseball/baseball.py --Team [MLB Team]`










