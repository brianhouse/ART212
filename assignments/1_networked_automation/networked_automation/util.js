const Twitter = require('twit')
const path = require('path')
const fs = require('fs')
const request = require('request')

const config = require('./config.js')
const print = console.log

const client = new Twitter(config)


function postTweet(text, callback) {
	client.post('statuses/update', {status: text},  function(error, tweet, response) {
		if (error) throw error
		callback(tweet)
	})
}

function postImageTweet(text, image_path, callback) {
	let b64content = fs.readFileSync(image_path, { encoding: 'base64' })
	client.post('media/upload', { media_data: b64content }, function(error, data, response) {
		if (error) throw error
		let media_ids = new Array(data.media_id_string)
		client.post('statuses/update', {media_ids: media_ids, status: text}, function(error, tweet, response) {
			if (error) throw error
			callback(tweet)
		})
	})
}

function download(uri, filename, callback) {
  request.head(uri, function(err, res, body) {
	// print('content-type:', res.headers['content-type'])
    // print('content-length:', res.headers['content-length'])
    request(uri).pipe(fs.createWriteStream(filename)).on('close', callback)
  })
}

function search(q, callback) {
	client.get('search/tweets', {q: q, count: 100, result_type: 'recent', include_entities: true}, function(error, data, response) {
		if (error) throw error
		let tweets = data.statuses
		for (let tweet of tweets) {
			if (tweet.entities.media != undefined) {
				let image_url = tweet.entities.media[0].media_url
				let tokens = image_url.split('/')
				download(image_url, "images/" + tokens[tokens.length-1], function () {})
			}
		}
		callback(tweets)
	})
}

exports.postTweet = postTweet
exports.postImageTweet = postImageTweet
exports.search = search
