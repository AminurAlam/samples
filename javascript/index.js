// single line comment

/*
* multi line comment
* write anything here
*/




//// printing something to console ////

console.log("hello world");
console.log(`i am printing
multiple lines`);
console.log(`sum of 1 and 2 is ${1+2}`);




//// variables and objects ////
//
//    var      changeable, global scope
//    let      changeable, local scope
//    const    unchangeable, local scope

// defining variables
let text = "example",
	number = 5,
	bool = true,
	undef,
	nothing = null;

// changeable & unchangeable variables
let value1 = "some value";
value1 = "other value";         // we can change the value again
const value2 = "some value";    // changing the value gives error

// some predefined variables
console.log(process.platform);
console.log(process.env.USER);

// getting type of a variable
console.table([
	// string
	{value: "text", type: typeof "text"},
	// number
	{value: 256, type: typeof 256},
	// boolean
	{value: true, type: typeof true},
]);

// deleting variables
var useless = "nothing";
delete useless;




//// string manipulation ////

let str = "this is a line of string";

str.length;         // 24
str.slice(0,14);    // "this is a line"




//// array ////

// creating an array
const animals = [ 'dog', 'cat', 'horse' ];

// logging array
console.log(animals);
console.table(animals);

// adds item to the end -> [ 'dog', 'cat', 'horse', 'monkey', 'fish' ]
animals.push('monkey');
animals.push('fish');

// removes last item in array and returns it -> 'fish'
animals.pop();

// removes item at an index -> [ 'dog', 'cat', 'horse' ]
delete animals[3];

// adds item at the beginning -> [ 'frog', 'dog', 'cat', 'horse' ]
animals.shift('frog');

// removes the first item -> [ 'dog', 'cat', 'horse' ]
animals.unshift();

// making copy of an array -> [ 'dog', 'cat', 'horse' ]
let animalsCopy = [...animals];

// accessing items from array - by indexing
let first = animals[0],
	second = animals[1];

// accessing items from array - by deconstruction
[first, second, third] = animals;

// checks whether it is an array -> true/false
Array.isArray(animals);

// concatenating arrays -> [ 'dog', 'cat', 'horse', 'bear', 'snake' ]
animalsCopy = animals.concat(['bear', 'snake']);

// finds the matching item and returns its index -> 2
animals.indexOf('horse');

// checks for item in array -> true/false
animals.includes('monkey');

// joins items seperated  by a string -> dog, cat, horse,
animals.join(', ');

// joins items with ',' -> dog,cat,horse
animals.toString();

// creates an empty array and fills it -> [ "item", "item", "item" ]
Array(3).fill("item")

// loops over each item -> index - animalName
animals.forEach(item => console.log(item));

animals.forEach(function (animal){
		console.log(animals.indexOf(animal), '-', animal);
    }
);




//// object ////

// creating object
const obj = {
	num: 10,
	name: "John Doe",
	country: "Canada",
};

// printing object
console.log(obj);
console.table(obj);

// adding item to object
obj.age = 30;

// removing item from object
delete obj.age;

// accessing items - dot and bracket notation
name = obj.name;
country = obj['country'];
console.log(name, "is from", country);

//deconstructing
let {name:name2 , country:country2} = obj;
console.log(name2, "is from", country2);




//// function ////

//defining function
function findLength(data) {
	console.log(`${data} is ${data.length} characters long`);
}

function add(num1,num2) {
  let result = num1 + num2;
  console.log(`sum of ${num1} and ${num2} is ${result}`);
  return result;
}

//calling function
findLength("fish");
add(5,7);

// anonymous function

anon = function () {
	console.log("hello anon");
}

anon();




//// statements ////

// if-else
if (1>0) {
    console.log("true");
} else {
	console.log("false");
}

// if-else short syntax
let age = 18;

console.log( age > 50 ? "old" : "young" );
age < 18 ? console.log("too young") : console.log("adult");

// try-catch
try {
	unknownFunction();
} catch (error) {
	console.log("error occured!");
}




//// cryptography ////

// base64
let msg = "secret text",
	msgEnc = "c2VjcmV0IHRleHQ=";

console.log(
	"\nencoded message:", btoa(msg),
	"\ndecoded message:", atob(msgEnc),
);





////launching html pages on localhost
const express = require("express");    //importing
const app = express();

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html");
    }
);

app.get("/fish.png", (req, res) => {
	res.sendFile(__dirname + "/res/fish.png");
    }
);


app.listen(3000, () => {
	console.log("index.html is launched at port 3000");
	console.log("go to http://127.0.0.1:3000");
})
