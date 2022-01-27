import esp32
import network
import machine
import urequests
import ujson
from time import sleep
from credentials import *

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            pass
    print("--> connected")


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

  #   digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on
  # digitalWrite(LED_BUILTIN, LOW);    // turn the LED off


# temp = esp32.raw_temperature()
# hall = esp32.hall_sensor()


#https://io.adafruit.com/api/docs/#create-data
