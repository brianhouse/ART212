const db = require('./db.js')
const print = console.log


// db.insert('people', {name: 'Sam', role: 'TA'})

db.retrieve('people', {name: 'Sam'}, readResults)

function readResults(result) {
    for (let entry of result) {
        print(entry)
    }
}
