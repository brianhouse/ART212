const AIO_USERNAME = "h0use"
const AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e"

function setup() {
    let canvas = createCanvas(640, 480)
    canvas.parent('p5')

    // low framerate
    // frameRate(1)
    noLoop()
}

async function draw() {

    // fetch our data
    let data = await fetchData("sensor-test")      // note the "await" keyword
    print(data)

    // resort it by time
    data.sort((a, b) => (a.created_at > b.created_at) ? 1 : -1)

    // make a new array with just the sensor values
    let values = []
    for (let datum of data) {
        values.push(datum.value)
    }

    // find the highest and lowest value
    let max_value = max(values)
    let min_value = min(values)
    // print("max_value " + max_value)
    // print("min_value " + min_value)

    // normalize the values between 0 and 1
    for (let i=0; i<values.length; i++) {
        let value = values[i]
        values[i] = (value - min_value) / (max_value - min_value)
    }

    //// now we have a set of values between and 0-1
    //// let do the same for the times

    // make a new array with just the timestamp
    let times = []
    for (let datum of data) {
        // convert the string into numerical time
        let time = Date.parse(datum.created_at) / 1000
        times.push(time)
    }
    // print(times)

    // find the and end time
    let start_time = min(times)
    let stop_time = max(times)

    // normalize the times to between 0 and 1
    for (let i=0; i<times.length; i++) {
        let time = times[i]
        times[i] = (time - start_time) / (stop_time - start_time)
    }

    // now we can draw

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

}

async function fetchData(feed) {
    return await new Promise((resolve, reject) => {
        let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
        httpGet(url, 'json', false, function(data) {
            resolve(data)
        })
    })
}
