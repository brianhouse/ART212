boot.py is run at boot
main.py is run next, which is the program

https://docs.micropython.org/en/latest/esp32/quickref.html


https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts

13 - This is GPIO #13 and also an analog input A12 on ADC #2. It's also connected to the red LED next to the USB port


jittery pots because 3.3 is going to be more sensitive than 5v
https://electronics.stackexchange.com/questions/516888/10k-potentiometer-with-arduino-uno-and-5v-works-but-same-pot-with-esp32-and-3-3v

awesome ref:
https://www.coderdojotc.org/micropython/sound/02-play-tone/

### output futures

outputs
- piezo (PWM)
- motor
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
