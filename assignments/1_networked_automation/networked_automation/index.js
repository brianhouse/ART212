const {postTweet, postImageTweet, search} = require('./util.js')
const print = console.log

print("Hello World")


search("grammys", readResults)

function readResults(tweets) {
    for (let tweet of tweets) {
        print(tweet.id)
        print(tweet.user.screen_name)
        print(tweet.text)
        print()
    }
}

//
// postTweet("Hello World"), function(tweet) {
//     print(tweet)
// })

//
// postImageTweet("just a test", "pio.jpg", function(tweet) {
//     print(tweet)
// })
