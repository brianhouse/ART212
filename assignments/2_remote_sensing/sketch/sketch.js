const AIO_USERNAME = "h0use"
const AIO_KEY = "2507ddf88a73494884935ca76ed2ae0e"

function setup() {
    // put setup code here
    let canvas = createCanvas(640, 480)
    canvas.parent('p5')

    requestData("office-temp")
    // sendData("office-temp", 100)

}

function draw() {
    // put drawing code here


}


function requestData(feed) {
    let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
    httpGet(url, 'json', false, receiveData, httpError)
}

function sendData(feed, value) {
    let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
    httpPost(url, 'json', {'X-AIO-Key': AIO_KEY, value: value}, receiveData, httpError)
}

function receiveData(data) {
    console.log(data)
}

function httpError(error) {
    console.log(error.toString())
}
