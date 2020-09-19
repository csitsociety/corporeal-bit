# Corporeal Bit Bot

A real life Bit robot, with an oled panel and other various sensors and outputs.

<p align="center">
<img src="https://github.com/csitsociety/corporeal-bit/blob/master/preview.jpg?raw=true" width="300">
</p>

## Environment

Bit's code runs on a Raspberry Pi Zero W, written in Python.

### Equipment
- [Winstar WEG010016A](https://www.winstar.com.tw/products/oled-module/graphic-oled-display/weg010016a.html) oled display
- [Raspberry pi camera module](https://au.element14.com/raspberry-pi/rpi-camera-board/raspberry-pi-camera-board-5mp/dp/2302279)
- [Adafruit I2S MEMS Microphone](https://www.adafruit.com/product/3421)
- More coming soon...

#### Wiring
GPIO pin number | GPIO pin name | Component pin | Component
---|---|---|---
1 | 3v3 Power | 3v | I2S MEMS Mic
2 | 5v Power | 2 (5V) | Winstar OLED WEB010016A
6 | Ground | 1 (GND) | Winstar OLED WEB010016A
9 | Ground | 5 (R/W) | Winstar OLED WEB010016A
12 | GPIO 18 (PCM CLK) | BCLK | I2S MEMS Mic
13 | GPIO 27 | 14 (D7) | Winstar OLED WEB010016A
14 | Ground | GND | I2S MEMS Mic
15 | GPIO 22 | 5v | Piezo Buzzer
16 | GPIO 23 | 13 (D6) | Winstar OLED WEB010016A
18 | GPIO 24 | 12 (D5) | Winstar OLED WEB010016A
20 | Ground | GND | Piezo Buzzer
22 | GPIO 25 | 11 (D4) | Winstar OLED WEB010016A
24 | GPIO 8 | 6 (CE) | Winstar OLED WEB010016A
26 | GPIO 7 | 4 (RS) | Winstar OLED WEB010016A
35 | GPIO 19 (PCM FS) | LRCL | I2S MEMS Mic
38 | GPIO 20 (PCM DIN) | DOUT | I2S MEMS Mic
39 | Ground | SEL | I2S MEMS Mic


## Setup

1. Clone the repository.
2. Run `pip install -r requirements.txt` to install the requirements.
3. Run `python main.py` in Bit's brain.

---
Maintained by the [RMIT CSIT Society](https://csitsociety.club).
