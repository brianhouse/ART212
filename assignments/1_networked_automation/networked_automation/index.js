const {postTweet, postImageTweet, search} = require('./util.js')
const print = console.log

print("Hello World")


search("bernie", readResults)

function readResults(tweets) {
    for (let tweet of tweets) {
        print(tweet.id)
        print(tweet.user.screen_name)
        print(tweet.text)
        print()
    }
}

//
// postTweet("just a test"), function(tweet) {
//     print(tweet)
// })

//
// postImageTweet("just a test"), ***, function(tweet) {
//     print(tweet)
// })
