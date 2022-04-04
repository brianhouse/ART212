boot.py is run at boot
main.py is run next, which is the program


https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts

https://docs.micropython.org/en/latest/esp32/quickref.html

https://www.coderdojotc.org/micropython/sound/02-play-tone/

https://awesome-micropython.com

### output futures

outputs
- motor
- neopixels
from neopixel import NeoPixel

what's in-between?
- mapping
- delays
- state machines (nonlinear-narrative)

need an intro of basic electronics info? maybe no.


https://github.com/micropython-IMU/micropython-fusion

https://microcontrollerslab.com/micropython-mpu-6050-esp32-esp8266/

I2C: eye-squared-see

Inertial Measurement Unit (IMU)

### wifi

digitalmediastudio
212212212

check for open ports:
nc -vnzu 10.4.15.228 1-8000


### accels

MPU-6050
accel + gyro (6 degrees)




copy folders

ampy --port /dev/tty.usbserial-01D5EBF4 put uosc

ls /dev/tty.*
