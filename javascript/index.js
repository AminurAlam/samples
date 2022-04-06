//single line comment

/*
multi line comment
write anything here
exit*/




////printing something to console

console.log("hello world");
console.log(`i'm printing
multiple lines`);
console.log(`sum of 1 and 2 is ${1+2}`);




////variables and objects
//
//    var      changeable, global scope
//    let      changeable, local scope
//    const    unchangeable, local scope

//defining variables
let text = "example";
let number = 5;
let bool = true;
let undef;
let nothing = null;

//changeable & unchangeable variables
let value1 = "some value";
value1 = "other value";         //we can change the value again
const value2 = "some value";    //changing the value gives error

//some predefined variables
console.log(process.platform);
console.log(process.env.USER);

//deleting variables
var useless = "nothing";
delete useless;




//nothing importaint here
let index;
let name;
let country;
let age;




////array object

//creating an array
const array = [ 10, "John Doe", "Canada" ];

//adding item to array
array.push(30);

//removing item from array
delete array[3];

//making copy of an array
const array2 = [...array];

//accessing items from array
//by indexing
name = array[1];
country = array[2];
console.log(`i am ${name} from ${country}`);

//accessing items from array
//by deconstruction
[index, name, country] = array;
console.log(`i am ${name} from ${country}`);




////dictionary object

//creating object
const obj = {
	index: 10,
	name: "John Doe",
	country: "Canada",
};

//adding item to object
obj.age = 30;

//removing item from object
delete obj.age;

//accessing items
//by dot and bracket notation
name = obj.name;
country = obj['country'];
console.log(name, "is from", country);

//deconstructing
let {name:name2 , country:country2} = obj;
console.log(name2, "is from", country2);




////function

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




////launching html pages on localhost
const express = require("express");    //importing
const app = express();

app.get(
  "/", 
  function (req, res) {
    res.sendFile(__dirname + "/index.html");
  }
);

app.listen(
  3000,
  function () {
    console.log("index.html is launched at port 3000");
    console.log("go to http://127.0.0.1:3000");
  }
);
