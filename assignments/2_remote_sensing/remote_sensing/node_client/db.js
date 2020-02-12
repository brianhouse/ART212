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
    await client.connect()
    print("Opened connection to database")
    const db = client.db(dbName)
    return await new Promise((resolve, reject) => {
        db.collection(collection).insertOne(data, function(error, response) {
            if (error) throw error
            print(`Inserted an entry into ${collection}`)
            client.close()
            print("Closed connection to database")
            resolve(response)
        })
    })
}

const retrieve = async function (collection, query) {
    await client.connect()
    print("Opened connection to database")
    const db = client.db(dbName)
    return await new Promise((resolve, reject) => {
        db.collection(collection).find(query).toArray(function(error, results) {
            if (error) throw error
            print(`Got ${results.length} entries from ${collection}`)
            client.close()
            print("Closed connection to database")
            resolve(results)
        })
    })
}

module.exports = {
    insert: insert,
    retrieve: retrieve,
}
