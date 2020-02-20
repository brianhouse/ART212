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
