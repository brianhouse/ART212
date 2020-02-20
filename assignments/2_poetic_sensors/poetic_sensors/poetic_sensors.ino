// load libraries
#include <WiFi.h>
#include <HTTPClient.h>

// add credentials
const char* WIFI_SSID = "LC Wireless";
const char* WIFI_PASS = "";
const String AIO_USERNAME = "h0use";
const String AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e";
const String AIO_FEED = "sensor-test";
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
    sendData(fsr_value); 
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
  delay(2000); // delay 2 seconds to avoid AIO rate limit
}
