const AIO_USERNAME = "h0use"
const AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e"

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
            values.push(datum.value / 10)   // change "10" to the max expected value for your data
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
