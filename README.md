# Corporeal Bit Bot

A real life Bit robot, with an oled panel and other various sensors and outputs.

<p align="center">
<img src="https://github.com/csitsociety/corporeal-bit/blob/master/preview.jpg?raw=true" width="300">
</p>

## Environment

Bit's code runs on a Raspberry Pi Zero W, written in Python.

#### Equipment
- [Winstar WEG010016A](https://www.winstar.com.tw/products/oled-module/graphic-oled-display/weg010016a.html) oled display
- [Raspberry pi camera module](https://au.element14.com/raspberry-pi/rpi-camera-board/raspberry-pi-camera-board-5mp/dp/2302279)
- More coming soon...


## Setup

1. Clone the repository.
2. Run `pip install -r requirements.txt` to install the requirements.
3. Run `python main.py` in Bit's brain.

#### Screen wiring
WEG010016A | Raspberry Pi
---|---
Pin 1 (GND) | GND
Pin 2 (5V) | 5V
Pin 4 (RS) | GPIO 7
Pin 5 (R/W) | GND
Pin 6 (E) | GPIO 8
Pin 11 (DB4) | GPIO 25
Pin 12 (DB5) | GPIO 24
Pin 13 (DB6) | GPIO 23
Pin 14 (DB7) | GPIO 27

---
Maintained by the [RMIT CSIT Society](https://csitsociety.club).
