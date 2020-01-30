# Project #1: Networked Automation

Much of the interaction that happens online is not between people, but between people and algorithms, or even between algorithms and algorithms. For example, huge platforms like Facebook, Google, and Twitter are constantly monitoring our activity and manipulating our feeds accordingly—and these platforms provide the environment for third-parties to attempt to game the system. From benign bots that tweet jokes to malicious fake followers that sow disinformation, we're not not alone out there.

In this project, you will create an experimental "Twitter Bot" using [Node.js](https://nodejs.org/en/) (or another programming language with instructor approval). Your bot will maintain a presence online by posting text and/or images, and it may interact socially by replying to others' comments. It may or may not be apparent to others that your bot is automated. It must have an underlying artistic concept that you can articulate in a 3-sentence artistic statement.

This is a 3-week project. This week your group will present a proposal of your idea to the class for feedback. Next week, your group will present your progress. The following week will be a crit.


## Groups

For this project, we'll be working in following groups:
- Andrew, Badral, Sam Sanford
- Ethan, Evelyn, Mo, Nabil
- Daniel, Jens, Shannon
- Dae, Jamie, Sam Flores
- Elias, Falcon, Leon


## Code

For this project, we'll be using [Node.js](https://nodejs.org/en/). Node is Javascript, but instead of running in the browser to make graphics like [p5](https://p5js.org), in runs on the command line. Unlike the graphics programming we did in Digital Media I, this is called "server-side" programming.

### Setup
- Download install [Node](https://nodejs.org/en/download/)
- Download and unzip the [template](https://github.com/brianhouse/networked_automation/releases)
- Copy `config.js.smp` to `config.js` in the template directory, and fill in the latter with your Twitter key information
- On MacOS, open the Terminal (`/Applications/Utilities/Terminal.app`) and practice navigating:
	- `pwd` shows the path of your current directory
	- `ls`  lists the content of your current directory
	- `cd`  followed by a space and a name changes to that directory
	- `cd ..`  moves backward into the enclosing directory
- On Windows, open the Command Prompt and practice navigating:
	- `D:`  changes to the D drive
	- `dir` lists the content of your current directory
	- `cd`  followed by a space and a name changes to that directory
	- `cd ..`  moves backward into the enclosing directory
- Run the example by typing `node index.js` in the "networked_automation" directory


### String functions in javascript
```js
let s = "I am a Twitter bot"

s.includes("bot")		// check if s includes the given string (true)
s.startsWith("bot")		// check if s starts with the given string (false)
s.endsWith("bot")		// check if s ends with the given string (true)

let words = s.split(" ")	// split the string into words (['I', 'am', 'a', 'Twitter', 'bot'])
s = words.join(" ")		// join an array of strings into a new long string

s = s.replace("Twitter bot", "real boy") // replace one substring with another and return a new string

s.toUpperCase() 		// I AM A REAL BOY
s.toLowerCase() 		// i am a real boy

```

### Arrays and loops in javascript
```js

let students = ["Ethan", "Shannon", "Dae", "Falcon"]	// declare an array

students[0] 			// "Ethan"
students[2] 			// "Dae"
students.slice(1, 2) 		// ["Shannon", "Dae"]

for (let i=0; i<students.length; i++) {	// loop through the array by index
	print(students[i])
}

for (let student of students) {		// loop through the array by element
	print(student)
}

students.push("Elias")			// add an element to the array
let student = students.pop()		// remove the last element of the array ("Elias")

```

### Objects in javascript
```js

// make a new object and store it in a variable
let student = {name: "Daniel", favorite_course: "lunch"}

// print out attributes of the object
print(student.name)					// "Daniel"
print(student.favorite_course)			// "lunch"

// make an array of objects
let students = [
	{name: "Daniel", favorite_course: "Lunch"},
	{name: "Sam", favorite_course: "Digital Media II"},
	{name: "Andrew", favorite_course: "Intro to Marxist Poetry"},
]

// loop over the array and print out object attributes
for (let student in students) {
	print(student.favorite_course)
}

/*
"Lunch"
"Digital Media II"
"Intro to Marxist Poetry"
*/

```

## Data

Botmaster [Darius Kazemi](http://tinysubversions.com/) has made a [resource](https://github.com/dariusk/corpora/tree/master/data) with various collections of words that could be useful for you projects.

Note that these collections are already formatted in a way that will work with your javascript code—they are usually formatted as lists inside objects. Just save them into a .js file in your folder and load them into your programs.

For example, this is a list of verbs: https://github.com/dariusk/corpora/blob/master/data/words/verbs.json

If you look at the file, the outermost layer is formatted as an object. So to get the list of words, we have to use the dot syntax (`.verbs`) when loading the file. It also includes both present and past tenses.

```js
let verbs = util.loadData("verbs.json").verbs
let verb = util.choice(verbs)
print(verb.present)
print(verb.past)

```

[Allison Parrish](https://www.decontextualize.com), a poet who works extensively with computation, provides a [tool]((http://static.decontextualize.com/lines-to-json/)) to convert plain lines of text to arrays. So, for example, if you find a list somewhere with the names of superheroes, you can convert it into a format that you can use in javascript without having to add in a bunch of quotes and commas yourself.


## Technical References

- [Twitter API](https://developer.twitter.com/en/docs/api-reference-index)
- [Javascript arrays](https://javascript.info/array)
- [Corpora](https://github.com/dariusk/corpora/tree/master/data)
- [Lines-to-JSON](http://static.decontextualize.com/lines-to-json/) utility
- [Crontab](https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html)

## Conceptual References

Examples of artist-made bots:
- [Constant Dullart](https://www.constantdullaart.com/), [_The Possibility of Raising an Army_](http://army.cheap), article in the [Guardian](https://www.theguardian.com/artanddesign/2015/nov/09/army-for-hire-the-artist-employing-ghost-soldiers-to-invade-facebook-constant-dullaart)
- [Ramsey Nasser](https://nas.sr), [_Top Gun 555µhz_](https://nas.sr/555µhz/)
- [Darius Kazemi](http://tinysubversions.com)
    - https://twitter.com/BodegaBot
    - https://twitter.com/moonshotbot
    - https://twitter.com/WhichOneBot
    - https://twitter.com/rapnamebot
    - https://twitter.com/EatenBot
- [Everest Pipkin](https://everest-pipkin.com) and Loren Schmidt, [Moth Generator](https://twitter.com/mothgenerator)
- Allison Parrish, [Deep Question Bot](https://twitter.com/deepquestionbot)
- Brian House and [Kyle McDonald](http://kylemcdonald.net), [_Conversnitch_](https://brianhouse.net/works/conversnitch/)
- https://twitter.com/greatartbot
- https://twitter.com/tinycarebot
- https://twitter.com/infinite_scream


Artist writing about how to make a good bot:
- Data and Society, "[How to Think About Bots](https://points.datasociety.net/how-to-think-about-bots-1ccb6c396326)"
- Harry Josephine Giles, "[Some Strategies of Bot Poetics](https://harryjosephine.com/2016/04/06/some-strategies-of-bot-poetics/)"
- Darius Kazemi, "[Basic Twitter Bot Etiquette](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/)"


Articles on malicious bots:
- https://www.bbc.com/news/technology-50817561
- https://duo.com/blog/anatomy-of-twitter-bots-fake-followers
- Lindy West, "[I’ve left Twitter. It is unusable for anyone but trolls, robots and dictators](https://www.theguardian.com/commentisfree/2017/jan/03/ive-left-twitter-unusable-anyone-but-trolls-robots-dictators-lindy-west)"
