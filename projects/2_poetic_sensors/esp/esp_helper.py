import esp32
import network
import urequests
import ujson
import time
import socket
from machine import ADC, Pin, TouchPad, PWM
from dht import DHT11
from time import sleep, time
from credentials import *

A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
D32 = Pin(32)
D33 = Pin(33)
S21 = Pin(21, Pin.OUT)
S27 = Pin(27, Pin.OUT)
LED = Pin(13, Pin.OUT)
T12 = TouchPad(Pin(12))
T14 = TouchPad(Pin(14))
T15 = TouchPad(Pin(15))
BAT = ADC(Pin(35), atten=ADC.ATTN_11DB)

battery_t = 0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect_wifi():
    if not wlan.isconnected():
        while True:
            print("Connecting to network...")
            LED.on()
            try:
                wlan.connect(SSID, PASS)
                while not wlan.isconnected():
                    LED.off() if LED.value() else LED.on()
                    sleep(1)
                print("--> connected")
                LED.off()
                break
            except Exception as e:
                print("Error: " + str(e))
                LED.off()
                sleep(1)


def check_battery():
    global battery_t
    t = time()
    if t - battery_t > 5 * 60:
        battery_level = (BAT.read() / 4096.0) * 3.3;
        print(f"Battery at {battery_level}")
        post_data("battery", battery_level)
        battery_t = t


def touch(pin):
    try:
        if pin == 12:
            return T12.read()
        elif pin == 14:
            return T14.read()
        elif pin == 15:
            return T15.read()
        else:
            print("Not a touch pin")
            return 0
    except ValueError as e:
        return 0


def post_data(feed, datum):
    print("Posting data... ")
    LED.on()
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
    LED.off()


def stream_data(data, ip, port=5005):
    sock.sendto(str(data).encode('utf-8'), (ip, port))


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


# temp = esp32.raw_temperature()
# hall = esp32.hall_sensor()

# https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts
