const AIO_USERNAME = "h0use"
const AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e"


function setup() {
    let canvas = createCanvas(640, 480)
    canvas.parent('p5')
    frameRate(1)
}

async function draw() {

    let data = await requestData("office-temp")

    // make a new array with just the numerical values
    let values = []
    for (let datum of data) {
        values.push(datum.value)
    }

    // find the highest and lowest value
    let max_value = max(values)
    let min_value = min(values)
    // print("max_value " + max_value)
    // print("min_value " + min_value)

    // normalize the values
    for (let i=0; i<values.length; i++) {
        let v = values[i]
        v = (v - min_value) / (max_value - min_value)
        v *= height
        values[i] = v
    }


    background(255)

    // make lines
    for (let i=1; i<values.length; i++) {
        line(i-1, values[i-1], i, values[i])
    }


}
