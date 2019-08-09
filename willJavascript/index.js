// var apple = 3
// console.log("apple: " + apple)
// var facNum = 5
// var product = 1
// for(var index = 1; index <= facNum ; index++ ) {
//     product = index * product
// }
// console.log("Factorial of " + facNum + " is " + product)

function factorial( facNum ) {
    var product = 1
    for( let index = 1; index <= facNum; index++ ) {
        product = index*product
    }
    console.log("Factorial of " + facNum + " is " + product)
}

factorial(5)

var factorial1 = ( facNum ) => {
    var product = 1
    for( let index = 1; index <= facNum; index++ ) {
        product = index*product
    }
    console.log("Factorial of " + facNum + " is " + product )
}

factorial1(6)