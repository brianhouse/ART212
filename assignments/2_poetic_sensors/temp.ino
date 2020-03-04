// REQUIRES the "Adafruit DHT Sensor" library and "Adafruit Unified Sensor" library

// load libraries
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"
#define DHTTYPE DHT11
#define DHTPIN 33       // Digital pin connected to the DHT sensor

// add credentials
const char* WIFI_SSID = "LC Wireless";
const char* WIFI_PASS = "";
const String AIO_USERNAME = "";
const String AIO_KEY = "";

HTTPClient http;
DHT dht(DHTPIN, DHTTYPE);

// keep track of when we last checked the battery
unsigned long battery_check = 0;


void setup() {
  // start the serial connection and wait for it to open
  Serial.begin(115200);
  while(! Serial);
  // set up the LED, we'll use it to show when we're transmitting data
  pinMode(LED_BUILTIN, OUTPUT);
  dht.begin();
}


void loop() {

  // make sure we're connected and check the battery
  connectToWifi();
  checkBattery();

  float h = dht.readHumidity();
  float t = dht.readTemperature(true);
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  Serial.print(F("Humidity: "));
  Serial.println(h);
  Serial.print(F("%  Temperature: "));
  Serial.println(t);

  sendData("humidity", h);
  sendData("temperature", t);

  // delay for a minute
  delay(60 * 1000);

}


void connectToWifi() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.print("Connecting to wifi...");
    int i = 0;
    while (WiFi.status() != WL_CONNECTED) {
      if (i % 10 == 0) {
        WiFi.disconnect();
        delay(250);
        WiFi.begin(WIFI_SSID, WIFI_PASS);
      }
      delay(1000);
      Serial.print(".");
      i++;
    }
    Serial.println();
    Serial.println("--> connected");
  }
}

void sendData(String feed, float datum) {
  Serial.print("Sending data... ");
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on
  String url = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/" + feed + "/data";
  String object = "{\"X-AIO-Key\": \"" + AIO_KEY + "\", \"value\": " + datum + "}";
  http.begin(url);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(object);
  Serial.println(httpResponseCode);
  http.end();
  delay(2000); // delay 2 seconds to avoid AIO rate limit
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off
}

void checkBattery() {
  unsigned long t = millis();
  if (battery_check == 0 || t - battery_check > 5 * 60 * 1000) {
    float voltage = ((analogRead(A13) * 2) / 4096.0) * 3.3;
    Serial.print("Battery at ");
    Serial.print(voltage);
    Serial.println("v");
    sendData("battery", voltage);   // report battery level every 5 minutes
    battery_check = t;
  }
}
