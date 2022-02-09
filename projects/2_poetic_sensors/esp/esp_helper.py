import esp32
import network
import urequests
import ujson
import time
from machine import ADC, Pin
from dht import DHT11
from time import sleep
from credentials import *

A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
D32 = Pin(32)
D33 = Pin(33)
BAT = ADC(Pin(35), atten=ADC.ATTN_11DB)

battery_t = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def connect_wifi():
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            pass
        print("--> connected")


def check_battery():
    global battery_t
    t = time.time()
    if t - battery_t > 5 * 60:
        battery_level = (BAT.read() / 4096.0) * 3.3;
        print(f"Battery at {battery_level}")
        post_data("battery", battery_level)
        battery_t = t


def post_data(feed, datum):
    print("Posting data... ")
    url = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/" + feed + "/data"
    post_data = ujson.dumps({"X-AIO-Key": AIO_KEY, "value": datum})
    response = urequests.post(url, headers={"content-type": "application/json"}, data=post_data)
    messages = response.json()
    if response.status_code == 200:
        print("--> OK")
    elif 'error' in messages:
        print("Error: " + messages['error'])
    else:
        print(messages)
    response.close()
    sleep(2) # avoid rate limit


class Smoother():

    def __init__(self, factor):
        self.factor = factor
        self.readings = [0] * int(self.factor)
        self.index = 0

    def smooth(self, v):
        self.readings[self.index] = v
        self.index = (self.index + 1) % self.factor
        value = sum(self.readings) / float(self.factor)
        return value


# digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on
# digitalWrite(LED_BUILTIN, LOW);    // turn the LED off


# temp = esp32.raw_temperature()
# hall = esp32.hall_sensor()

# https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts
