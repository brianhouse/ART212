const config = require('./config.js')
const MongoClient = require('mongodb').MongoClient
const assert = require('assert')
const print = console.log

// connection URL
const url = `mongodb+srv://${config.db_username}:${config.db_password}@cluster0-70z0n.mongodb.net/test?retryWrites=true&w=majority`

// database name
const dbName = config.db_name

// create a new MongoClient
const client = new MongoClient(url, {useUnifiedTopology: true})

const insert = async function (collection, data, callback) {
    let response = await client.connect()
    print("Opened connection to database")
    const db = client.db(dbName)
    db.collection(collection).insertOne(data, function(error, response) {
        if (error) throw error
        print(`Inserted entry into ${collection}`)
        if (callback) {
            callback(response)
        }
        client.close()
        print("Closed connection to database")
    })
}

const retrieve = async function (collection, query, callback) {
    let response = await client.connect()
    print("Opened connection to database")
    const db = client.db(dbName)
    db.collection(collection).find(query).toArray(function(error, response) {
        if (error) throw error
        print(`Got ${response.length} entries from ${collection}`)
        if (callback) {
            callback(response)
        }
        client.close()
        print("Closed connection to database")
    })
}

module.exports = {
    insert: insert,
    retrieve: retrieve,
}
