#include "AdafruitIO_WiFi.h"

const char* WIFI_SSID = "your_ssid";
const char* WIFI_PASS = "your_pass";
const char* AIO_USERNAME = "your_username";
const char* AIO_KEY = "your_key";

AdafruitIO_WiFi io(AIO_USERNAME, AIO_KEY, WIFI_SSID, WIFI_PASS);
AdafruitIO_Feed *analog = io.feed("office-temp");


// analog pin 0
const int PHOTOCELL_PIN = A0;

// photocell state
int current = 0;
int last = -1;


void setup() {

  // start the serial connection
  Serial.begin(115200);

  // wait for serial monitor to open
  while(! Serial);

  // connect to io.adafruit.com
  Serial.print("Connecting to Adafruit IO");
  io.connect();

  // wait for a connection
  while(io.status() < AIO_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  // we are connected
  Serial.println();
  Serial.println(io.statusText());

}

void loop() {

  // io.run(); is required for all sketches.
  // it should always be present at the top of your loop
  // function. it keeps the client connected to
  // io.adafruit.com, and processes any incoming data.
  io.run();

  // grab the current state of the photocell
  current = analogRead(PHOTOCELL_PIN);

  // stop if the value hasn't changed
  if(current == last)
    return;

  // save the current state to the analog feed
  Serial.print("sending -> ");
  Serial.println(current);
  analog->save(current);

  // store last photocell state
  last = current;

  // wait three seconds (1000 milliseconds == 1 second)
  delay(3000);
}
