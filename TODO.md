- finish getting the reading up, with notes
- bot display on a raspi or something

### poetic sensors

- port to micropython?
http://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro

https://www.digikey.com/en/maker/projects/micropython-basics-load-files-run-code/fb1fcedaf11e4547943abfdd8ad825ce

```
ls /dev/tty.*

python3 -m pip install esptool --user

python3 -m esptool --chip esp32 --port /dev/tty.usbserial-01D1D9CE erase_flash

python3 -m esptool --chip esp32 --port /dev/tty.usbserial-01D1D9CE --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin

python3 -m pip install adafruit-ampy --user

ampy --help

ampy --port /dev/tty.usbserial-01D1D9CE run test.py
ampy --port /dev/tty.usbserial-01D1D9CE put main.py
ampy --port /dev/tty.usbserial-01D1D9CE get boot.py
ampy --port /dev/tty.usbserial-01D1D9CE ls
```
boot.py is run at boot
main.py is run next, which is the program

- how to install modules? --> do I need any other than the basics?
- do I need a driver? --> maybe not

- how to get print statements back via serial?

So only question is the data platform.
https://gpiocc.github.io/learn/micropython/esp/2020/05/23/martin-ku-upload-sensor-data-to-adafruit-io-with-esp32-and-micropython.html

...which works because it's rest.

shit.

so then it's a matter of loading. ideally, they could write the code in the processing IDE

this could probably all work the same with circuitpython

Thonny actually works well.
so... I test a machine that doesn't have a driver?
I think yes. https://pythonforundergradengineers.com/how-to-install-micropython-on-an-esp32.html#install-the-silabs-driver-for-the-cp210x-chip

REPL:
```screen /dev/tty.usbserial-01D1D9CE 115200```

https://docs.micropython.org/en/latest/esp32/quickref.html#installing-micropython

- can the data vis all be within processing?

- direct data reception by processing?


### pcomp futures

Consider 3D could be a separate 2-week mini unit, with double unit for sensors

inputs
- force
https://www.adafruit.com/product/166
https://www.adafruit.com/product/1070

- photocells
https://www.adafruit.com/product/161

- motion sensors
https://www.adafruit.com/product/172

- sound level (3v only)
https://www.adafruit.com/product/1713
-- use an FFT driver?

- temperature and humidity
https://www.adafruit.com/product/386
import dht

- heartrate
https://www.adafruit.com/product/1093
https://www.mfitzp.com/invent/wemos-heart-rate-sensor-display-micropython/

- touch
(built-in)

+ 10k resistors
+ breadboards



outputs
- piezo (PWM)
- motor
- LED
- neopixels
from neopixel import NeoPixel

what's in-between?
- mapping
- delays
- state machines (nonlinear-narrative)

need an intro of basic electronics info? maybe no.


### code

https://randomnerdtutorials.com/esp32-touch-pins-arduino-ide/
