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

// Sample window width in ms (50 ms = 20Hz, 1000 ms = 1hz)
const int window = 50;
unsigned int sample;

void setup() {
  // start the serial connection and wait for it to open
  Serial.begin(115200);
  while(! Serial);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

    // make sure we're connected and check the battery
    connectToWifi();
    checkBattery();

    unsigned long start_time = millis();  // Start of sample window
    unsigned int peak = 0;
    unsigned int low = 4096;

    // gather samples over a window and find the peak
    while (millis() - start_time < window) {
        sample = analogRead(SENSOR_PIN);
        if (sample < 4095) {      // ignore high signal glitches
          if (sample > peak) {
            peak = sample;
          } else if (sample < low) {
            low = sample;
          }
        }
    }
    float level = 100 * ((peak - low) / 4096.0);
    Serial.println(level);

    // if it's a relevant value, send it to AIO
    if (level > 5) {
      sendData("sound-level", level);
    }

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
  digitalWrite(LED_BUILTIN, HIGH);
  String url = "https://io.adafruit.com/api/v2/" + AIO_USERNAME + "/feeds/" + feed + "/data";
  String object = "{\"X-AIO-Key\": \"" + AIO_KEY + "\", \"value\": " + datum + "}";
  http.begin(url);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(object);
  Serial.println(httpResponseCode);
  http.end();
  delay(2000); // delay 2 seconds to avoid AIO rate limit
  digitalWrite(LED_BUILTIN, LOW);
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
