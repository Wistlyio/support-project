# starter notes
# 1.) How to declare variables
#     Make a variable called apple
#     Can or can you not assign a variable a string and then change its type to a number
# 2.) How to print 
#     Print "Hello world!"
# 3.) For loops
#     2 types: how to iterate through an array, how to print out array by indexes
#     Factorial for loop
# 4.) If statements
# 5.) Functions
#     Make the for loop a function
# 6.) Dictionary
#     var myObj = {name: "John", age: 31, city: "New York"}; In javascript
#     Make a dictionary of ^
# 7.) Classes
#     Make a person class

# Declaring a variable called apple, setting its value to be orange
apple = "orange"
# Yes you can assign a variable a string and later change its type to a number 
# because python doesn't have any "types," it just has variables in general

# Print using the print() command
print(apple)
print( "Hello world!" )

# Using a for loop to print an array 2 ways
animals = ["dog", "cat", "rat", "bat"]
for animal in animals:
    print(animal)

for number in range(2, 6):
    print(number)

# Use a for loop to create a factorial 
# in java: 
# for(int fac = 5; fac >= 0; fac--) {
#   int product = product * fac
# }
facNum = 5
product = 1
for i in range(0, facNum):
    product = product * facNum
    facNum -= 1
print(product)

# If statement 
a = 30
b = 100
if a < b:
    print( a, "is less than", b)
else:
    print("false")

# Factorial as a function
def factorial_function(factorial):
    products = 1
    for i in range(0, factorial):
        products = products * factorial
        factorial -= 1
    print(products)

factorial_function(5)

# Making a car dictionary
car = {
    "brand" : "Tesla",
    "model" : "X",
    "year"  : 2019
}
print(car)

house = {
    "location" : "address",
    "people" : "Stanley"
}

ticket = {
    "subject" : "parking",
    "time" : "2:09",
    "person" : "Stanley",
    "issuer" : "officer",
    "location" : "parking lot"
}

support = {
    "name" : "First and last",
    "issue" : "problem",
    "email" : "xyz@gmail.com",
    "description" : "details"
    "id" : "ticket number"
}

# Making a person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

p1 = Person("Stanley", 18 )
print(p1.name)
print(p1.age)
p1.change_name("William")
print(p1.name)