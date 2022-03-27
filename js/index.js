//single line comment

/*
multi line comment
*/

console.log("hello world")


//assigning values to a variable
let string = "string"
let num = 5
let bool = true
let undef
let nothing = null

let obj = {
  index: 1,
  name: "value"
}

let array = [1, "value"]

//printing the type of value
console.log("\n",
  bool, "is", typeof bool, "\n",
  undef, "is", typeof undef, "\n",
  nothing, "is", typeof nothing, "\n",
  obj, "is", typeof obj, "\n",
  array, "is", typeof array, "\n"
)

//changeable & unchangeable variables
let value1 = "some value"
value1 = "other value"

const value2 = "some value"


//dictionary object
obj = {
  index: 10,
  name: "John Doe",
  country: "Canada",
  age: 30
}
console.log(obj.name, "is from", obj['country'])

//array object
array = ["John Doe", "Canada", 30]


//functions
function findLength(data) {
  console.log(data, "is", data.length, "characters long")
}

findLength("hello world!");
