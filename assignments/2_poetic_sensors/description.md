# Project #2: Poetic Sensing

We connect to the internet with our laptops with our laptops and mobile phones. However, as of 2020, there are [30 billion devices connected to the internet](https://www.statista.com/statistics/471264/iot-number-of-connected-devices-worldwide/), far outstripping the human population. Most of these devices are sensors collecting data about the physical world, whether whether they are monitoring the environment, surveilling people, or directing the actions of innumerable machines. This is the "internet of things."

For this project, you will construct a sensor to gather data on some aspect of the world around you. These data will be transmitted to a server, and they will subsequently trigger an interaction with another platform and/or be interpreted with a visualization, sonification, or through some other means. To build a sensor, you will use a [ESP32 wireless microcontroller](https://www.espressif.com/en/products/hardware/esp32/overview) and the [Adafruit IO platform](https://io.adafruit.com). To work with the data, you may program something yourself using [p5](https://p5js.org) or [node][https://nodejs.org], use [IFTTT](http://ifttt.com/)(If-This-Then-That, no programming required), or work with some other set of tools.

This is a 3-week project that you will complete individually. This week you will present a proposal of your idea to the class for feedback. Next week, your will present your progress. The following week will be a crit.

You must have an underlying artistic concept that you can articulate in a 3-sentence artistic statement.

## Code

### Technical Setup

We will be using the Arduino platform to write code for our ESP32s:

- Download and install the [ESP driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
- Download and install the [Arduino IDE](https://www.arduino.cc/en/main/software)
- Add the ESP32 libraries
    - Start the Arduino IDE and open Preferences window
    - In the "Additional Boards Manager URLs" enter `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
    - Open Boards Manager from Tools > Board menu and install the esp32 platform by Espressif Systems
    - Select "Adafruit ESP32 Feather" ESP32 board from Tools > Board menu

The Adafruit IO platform provides us with a server:

- Sign up at https://io.adafruit.com
- Create a new "feed"


## Technical References

[Adafruit ESP32 Feather](https://learn.adafruit.com/adafruit-huzzah32-esp32-feather)

Basic approach to wiring sensors (use 3v instead of 5v, and analog inputs A2-A5 for now):
![](light_cdspulldowndiag.gif)

<!-- - [button](https://www.arduino.cc/en/tutorial/button)
- [FSR](https://learn.adafruit.com/force-sensitive-resistor-fsr) -->


## Arduino Code Template

```c++
// load libraries
#include <WiFi.h>
#include <HTTPClient.h>

// add credentials
const char* WIFI_SSID = "LC Wireless";
const char* WIFI_PASS = "";
const String AIO_USERNAME = "XXXXX";
const String AIO_KEY = "XXXXXXXXXX";
const String AIO_FEED = "XXXXX";
HTTPClient http;

// keep track of sensor pins
const int FSR_PIN = A2;


void setup() {
  // start the serial connection and wait for it to open
  Serial.begin(115200);
  while(! Serial);
}


void loop() {

  // make sure we're connected
  connectToWifi();

  // grab the current state of the sensor
  int fsr_value = analogRead(FSR_PIN);
  Serial.print("fsr_value -> ");
  Serial.println(fsr_value);

  // if it's a relevant value, send it to AIO
  if (fsr_value > 10) {
    //sendData(fsr_value);
  }

  // always include a short delay
  delay(50);

}

void connectToWifi() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.print("Connecting to wifi...");
    WiFi.begin(WIFI_SSID, WIFI_PASS);
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.print(".");
    }
    Serial.println();
    Serial.println("--> connected");
  }
}


void sendData(int datum) {
  Serial.print("Sending data... ");
  String url = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/" + AIO_FEED + "/data";
  String object = "{\"X-AIO-Key\": \"" + AIO_KEY + "\", \"value\": " + datum + "}";
  http.begin(url);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(object);
  Serial.println(httpResponseCode);
  http.end();  
  delay(30000); // delay 30 seconds to avoid AIO rate limit
}
```
