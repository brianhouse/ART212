const Twitter = require('twit')
const path = require('path')
const fs = require('fs')
const request = require('request')
const config = require('./config_.js')
const print = console.log

const client = new Twitter(config)

function post(text, callback) {
	client.post('statuses/update', {status: text},  function(error, tweet, response) {
		if (error) throw error
		callback(tweet)
	})
}

function reply(screen_name, tweet_id, text, callback) {
	screen_name = screen_name.replace('@', '')
	client.post('statuses/update', {status: "@" + screen_name + " " + text, in_reply_to_status_id: tweet_id},  function(error, tweet, response) {
		if (error) throw error
		if (callback) callback(tweet)
	})
}

function post_image(text, image_path, callback) {
	let b64content = fs.readFileSync(image_path, { encoding: 'base64' })
	client.post('media/upload', { media_data: b64content }, function(error, data, response) {
		if (error) throw error
		let media_ids = new Array(data.media_id_string)
		client.post('statuses/update', {media_ids: media_ids, status: text}, function(error, tweet, response) {
			if (error) throw error
			if (callback) callback(tweet)
		})
	})
}

function follow(screen_name, callback) {
	client.post('friendships/create', {screen_name: screen_name}, function(error, user, response) {
		if (error) throw error
		if (callback) callback(user)
	})
}

function retweet(tweet_id, callback) {
	client.post('statuses/retweet/' + tweet_id, {tweet_id: tweet_id}, function(error, tweet, response) {
		if (error) throw error
		if (callback) callback(tweet)
	})
}

function like(tweet_id, callback) {
	client.post('favorites/create', {id: tweet_id}, function(error, tweet, response) {
		if (error) throw error
		if (callback) callback(tweet)
	})
}

function timeline(callback) {
	client.get('statuses/home_timeline', {count: 20}, function(error, tweets, response) {
		if (error) throw error
		if (callback) callback(tweets)
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
				download(image_url, "downloaded_images/" + tokens[tokens.length-1], function () {})
			}
		}
		if (callback) callback(tweets)
	})
}

function download(uri, filename, callback) {
	request.head(uri, function(err, res, body) {
    	request(uri).pipe(fs.createWriteStream(filename)).on('close', callback)
  	})
}



exports.post = post
exports.post_image = post_image
exports.follow = follow
exports.retweet = retweet
exports.like = like
exports.reply = reply
exports.timeline = timeline
exports.search = search
