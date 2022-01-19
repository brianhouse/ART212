# Project #2: Poetic Sensing

As of 2020, there are [30 billion devices connected to the internet](https://www.statista.com/statistics/471264/iot-number-of-connected-devices-worldwide/), which far exceeds the human population. Most of these devices include sensors to capture data about the physical world, whether by monitoring the environment, surveilling people, or otherwise providing input to machines. While we may be largely unaware of their presence, these sensors and the systems of which they are a part end up shaping the world around us.

For this project, you will engage with sensor systems as an artistic medium. Choose some aspect of your physical environment and use a sensor to capture it—this could be as simple as how many times you sit at your desk, for example, or the amount of electromagnetic interference you pass during the day. These data will be transmitted to a server. Subsequently, you must interpret the data in some way, whether by visualizing it or using it to trigger some sort of action in the world.

To capture data, you will use a [ESP32 wireless microcontroller](https://www.espressif.com/en/products/hardware/esp32/overview) and the [Adafruit IO platform](https://io.adafruit.com). To interpret the data, you may program something yourself using [p5](https://p5js.org) or [node][https://nodejs.org], use [IFTTT](http://ifttt.com/)(If-This-Then-That, no programming required), or work with some other set of tools, including non-digital mediums.

This is a 3-week project that you will complete individually. This week you will present a proposal of your idea to the class for feedback. Next week, you will present your progress. The following week will be a crit. You must have an underlying artistic concept that you can articulate in a 3-sentence artistic statement that you will present with the work.


## Code (and Wiring)

### Setup

To write code for our ESP32s, we will be using the Arduino IDE:

- Download and install the [ESP driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
- Download and install the [Arduino IDE](https://www.arduino.cc/en/main/software)
- Add the ESP32 libraries
    - Start the Arduino IDE and open Preferences window
    - In the "Additional Boards Manager URLs" enter `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
    - Open Boards Manager from Tools > Board menu and install the esp32 platform by Espressif Systems
    - Select "Adafruit ESP32 Feather" ESP32 board from Tools > Board menu

The Adafruit IO platform provides us with a server:

- Sign up at https://io.adafruit.com
- Create a new "feed" called "sensor-test" and one called "battery"
- Note your AIO username and AIO key


### ESP32 Reference

The technical specs on the [Adafruit ESP32 Feather](https://learn.adafruit.com/adafruit-huzzah32-esp32-feather)

Use A2, A3, and A4 for analog inputs and 32 and 33 for GPIOs. The other pins have various other functionality attached to them and may not work initially as expected.


### Basic Sensors
The following is a basic template for reporting a sensor value. This applies to force-sensitive resistors (bending or touching), photocells (light level), and motion sensors (presence). You will also need a 10k Ohm resistor.

##### Arduino Template
[basic.ino](basic.ino)

##### Wiring
![](basic.jpg)


### Sound Level

You can monitor sound level with the [MAX9814](https://www.adafruit.com/product/1713). This setup sends a value when sound reaches above a certain threshold. For ambient sound level monitoring, set `window` to 1000 and take out the conditional around `sendData` in the code.

##### Arduino Template
[sound_level.ino](sound_level.ino)

##### Wiring
![](sound_level.jpg)


### Temperature and Humidity

This variation works with [DHT11 (blue) breakout boards](https://www.amazon.com/HiLetgo-Temperature-Humidity-Digital-3-3V-5V/dp/B01DKC2GQ0/ref=sr_1_4?crid=29K0T2RXDWMKE&dchild=1&keywords=dht11+temperature+and+humidity+sensor&qid=1582840745&sprefix=DHT11%2Caps%2C204&sr=8-4). You'll also need to install the "Adafruit DHT Sensor" library and "Adafruit Unified Sensor" library through the Arduino IDE library manager (make sure these titles match exactly—there are a lot of similarly named modules). Connect the "out" pin from the sensor to pin 33 on your ESP32.

##### Arduino Template
[temp.ino](temp.ino)

##### Wiring
![](temp.jpg)


### Heart Rate

A [Pulse Sensor](https://www.adafruit.com/product/1093) can be used to monitor your heart rate. Note that the sensor works best when the back is covered by something opaque like a piece of electrical tape, and try putting it on your earlobe—read the online guides at [PulseSensor.com](http://PulseSensor.com). You will need to install the PulseSensor Playground library through the Arduino IDE library manager. Look at the live data using the Serial Plotter; this code reports a BPM every minute.

##### Arduino Template
[pulse.ino](pulse.ino)


##### Wiring
![](pulse.jpg)


### p5 Template (Data Visualization)

You will need to make your feed public to retrieve the data using javascript.

```js
const AIO_USERNAME = ""
const AIO_KEY = ""

let values = []
let times = []

let index = 0

function setup() {

    let canvas = createCanvas(640, 480)
    canvas.parent('p5')

    // fetch our data
    let feed = 'sound-level'
    let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
    httpGet(url, 'json', false, function(data) {

        print(data)
        // re-sort the array by time
        data.sort((a, b) => (a.created_at > b.created_at) ? 1 : -1)

        // make a new array with just the sensor values
        // divide by the max value to "normalize" them to the range 0-1
        for (let datum of data) {
            values.push(datum.value / 4095)
        }

        // make a new array with just the timestamp
        // this one is trickier to normalize so we'll do it separately
        for (let datum of data) {
            // convert the string into a numerical timestamp
            let time = Date.parse(datum.created_at) / 1000
            times.push(time)
        }

        // normalize the times to between 0 and 1
        let start_time = min(times)
        let stop_time = max(times)
        for (let i=0; i<times.length; i++) {
            let time = times[i]
            times[i] = (time - start_time) / (stop_time - start_time)
        }

    })

}

function draw() {

    background(255)

    // make colors
    // in this case, we want a line every pixel, and to interpolate between values
    // colorMode(HSB) // https://p5js.org/reference/#/p5/colorMode
    for (let i=1; i<values.length; i++) {
        let x1 = int(times[i-1] * width)
        let x2 = int(times[i] * width)
        print(x1, x2)
        let c1 = color(55, values[i-1] * 255, 255)
        let c2 = color(55, values[i] * 255, 255)
        for (let x=x1; x<=x2; x++) {
            let interpolation = (x-x1) / (x2-x1)
            print(x, interpolation)
            let c = lerpColor(c1, c2, interpolation)
            stroke(c)
            line(x, 0, x, height)
        }
    }

    // this one is just a breakpoint line, similar to the adafruit feed page
    // note that to get the y axis right, we have to flip it by subtracting from 1
    stroke(0)
    strokeWeight(2)
    for (let i=1; i<values.length; i++) {   // starting at 1, not 0
        let x1 = times[i-1] * width
        let y1 = (1 - values[i-1]) * height
        let x2 = times[i] * width
        let y2 = (1 - values[i]) * height
        line(x1, y1, x2, y2)
    }

    // try an animation
    circle(times[index] * width, (1 - values[index]) * height, 50)
    index += 1
    if (index == times.length) {
        index = 0
    }

}
```


### Node Template

You will need to make your feed public to retrieve the data using javascript.

```js
const request = require('request') // install with "npm install request"
const print = console.log

const AIO_USERNAME = "h0use"
const AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e"

// helper function to fetch a feed
async function fetchData(feed) {
    return await new Promise((resolve, reject) => {
        let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
        request(url, {json: true}, (error, response, body) => {
            resolve(body)
        })
    })
}

// do stuff in here
async function main() {

    let results = await fetchData("sensor-test")    // note: await
    print(results)

    for (let result of results) {
        print(result)
    }

}

main()
```


## Conceptual References
- [Nathalie Miebach](https://nathaliemiebach.com) (weather data)
- [Karolina Sobecka](http://cargocollective.com/karolinasobecka/filter/matterOfAir/Puff) (car exhaust)
- [Georgia Lupi](http://giorgialupi.com) (hand-drawn data visualization)
- [Martin Howse](http://www.1010.co.uk/org/radiomycelium.html) (mycelium)
- [Afroditi Psarra](http://afroditipsarra.com/index.php?/older-projects/cosmic-bitcasting/) (cosmic rays)
- [Jer Thorp](http://jerthorp.com/) (data visualization)
- [Ali Momeni](http://alimomeni.net/gutwise) (the gut)
- [Brian House](https://brianhouse.net/works/animas/) (water quality)
- [Chris Woebken](https://chriswoebken.com/Amphibious-Architecture) (fish)
- [Timo Toots](https://www.timo.ee/psa/) (ants)
