
async function requestData(feed) {
    return await new Promise((resolve, reject) => {
        let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
        httpGet(url, 'json', false, function(data) {
            resolve(data)
        })
    })
}

async function sendData(feed, value) {
    return await new Promise((resolve, reject) => {
        let url = `https://io.adafruit.com/api/v2/${AIO_USERNAME}/feeds/${feed}/data`
        httpPost(url, 'json', {'X-AIO-Key': AIO_KEY, value: value}, function(data) {
            resolve(data)
        })
    })
}
