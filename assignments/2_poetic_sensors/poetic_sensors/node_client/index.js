const db = require('./db.js')
const print = console.log

async function main() {

    // await db.insert('people', {name: 'Sam', role: 'TA'})

    let results = await db.retrieve('people', {name: 'Sam'})

    for (let result of results) {
        print(result)
    }

}

main()
