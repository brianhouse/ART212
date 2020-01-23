const Twitter = require('twit')
const path = require('path')
const fs = require('fs')
const request = require('request')

const config = require('./config.js')
const print = console.log

const client = new Twitter(config)
