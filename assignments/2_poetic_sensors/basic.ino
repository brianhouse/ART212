// load libraries
#include <WiFi.h>
#include <HTTPClient.h>

// add credentials
const char* WIFI_SSID = "LC Wireless";
const char* WIFI_PASS = "";
const String AIO_USERNAME = "";
const String AIO_KEY = "";
HTTPClient http;

// keep track of where the sensor is connected
const int SENSOR_PIN = A2;

// keep track of when we last checked the battery
unsigned long battery_check = 0;


void setup() {
  // start the serial connection and wait for it to open
  Serial.begin(115200);
  while(! Serial);
  // set up the LED, we'll use it to show when we're transmitting data
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {

  // make sure we're connected and check the battery
  connectToWifi();
  checkBattery();

  // grab the current state of the sensor
  //int value = digitalRead(SENSOR_PIN); // use this if it's just a trigger
  int value = analogRead(SENSOR_PIN);   // use this if you want the actual value
  Serial.print("value -> ");
  Serial.println(value);

  // modify this condition to fit your application
  // if you remove the condition entirely, it will send every 2 seconds
  // (for digital reads, you probably don't need a condition)
  if (value > 10) {
    // if it's a relevant value, send it to AIO
    // paramters for sendData are the AIO feed-key and the numerical value
    sendData("sensor-test", value);
  }

  // include a short delay for the circuit to stabilize
  delay(50);

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
