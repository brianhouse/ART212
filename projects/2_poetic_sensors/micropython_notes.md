### installation

```
ls /dev/tty.*

python3 -m pip install esptool --user

python3 -m esptool --chip esp32 --port /dev/tty.usbserial-01D1D9CE erase_flash

python3 -m esptool --chip esp32 --port /dev/tty.usbserial-01D1D9CE --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin

python3 -m pip install adafruit-ampy --user
```
boot.py is run at boot
main.py is run next, which is the program


https://docs.micropython.org/en/latest/esp32/quickref.html



### output futures

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


### next

can we stream data via wifi or bluetooth? that's the thing, right?

want UDP.

https://www.dfrobot.com/blog-608.html

right so it's just python.
does that work in processing?

shit, so that is potentially super straight forward.

would then need accelerometers, you know? and knobs.

that could possibly shift the whole thing.

ok. but not now.

https://github.com/micropython-IMU/micropython-fusion


https://awesome-micropython.com


### wifi

digitalmediastudio
212212212

check for open ports:
nc -vnzu 10.4.15.228 1-8000
