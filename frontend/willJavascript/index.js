// Work like imports 
const axios = require('axios')
const url = "https://75edb7de.ngrok.io"
/* Topics we went over */
// functions
// arrow functions ( => kind of a shortcut )
// loops
// oop
// promises (eg. the .then and .catch statements)
// async functions
// nodes
    // npm (eg. "npm start" to start program)
    // axios

// Use "code ." to open VS code
// Declare variables v
// var apple = 3
// console.log("apple: " + apple)
// var facNum = 5
// var product = 1
// for(var index = 1; index <= facNum ; index++ ) {
//     product = index * product
// }
// console.log("Factorial of " + facNum + " is " + product)

/* Can only be used in the scope, mutable */ 
var orange = 1

/* Can be used outside of its scope, similar to static, 
    mutable */
let banana = 5

/* Immutable, final constant */
const watermelon = 2

// Made a function that calculated the factorial of a number
function factorial( facNum ) {
    var product = 1
    for( let index = 1; index <= facNum; index++ ) {
        product = index*product
    }
    // Print out the value
    console.log("Factorial of " + facNum + " is " + product)
}

//factorial(5)

// Same function but with an arrow function
var factorial1 = ( facNum ) => {
    var product = 1
    for( let index = 1; index <= facNum; index++ ) {
        product = index*product
    }
    console.log("Factorial of " + facNum + " is " + product )
}

//factorial1(6)

// How to make a get request, promised based
var axiosGet = ( url ) => {
    axios.get( url ).then((response) =>{
    // handle success
    console.log(response.data);
    return response.data 
  })
  .catch((error) => {
    // handle error
    console.log(error);
  })
}

// Async functions for get request, this one waits for a response
var axiosGetAsync = async ( url ) => {
    return await axios.get( url )
}

// Test the get response
//var data = axiosGet("https://ae5d57c9.ngrok.io")
//console.log(data)

// Test the async get response 
//var dataAsync = axiosGetAsync("https://ae5d57c9.ngrok.io")
//console.log(dataAsync)

// Make a person class, make interface to get something
// like the name of the person, make an instance of it
class Person {
    constructor( name, age ) {
        this.name = name;
        this.age = age;
    }
    addTwo (one, two){
        return (one + two)
    }
}

var Maria = new Person( "Maria", 18)
// console.log(Maria.name)
// console.log(Maria.age)
console.log(Maria.addTwo(7,9))