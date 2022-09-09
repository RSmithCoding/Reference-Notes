# Printing messages

import math
print("This is a message to the screen")

print("=" * 10)

# Asinging values to Varibles and displaying

no_of_guests = 500
print(no_of_guests)

# Initger

example_i = 200

# Float

example_f = 9.99

# Boolean

example_b = True

# Text

example_t = "This is a string of text"

# Working with build in functions with strings

string = "Russell Smith"

print(len(string))  # Returns the amount of characters in the string

print(string[0:5])  # Returns so many characters in the string

print("This is how to use\" an escape character")

print("This is how to break a \nstring onto a new line")

# Formatted strings and Concantination

make = "Vauxhall"
model = "Corsa"

full_name = f"{make} {model}"  # Any expressions can also got in curly braces
print(full_name)

# Built in Methods on strings

print(string.find("s"))  # Finds charater in string and returns int index
print(string.replace("s", "!"))  # Replaces one character with another
# Checks to see is character or string is in the string and retruns True / False
print("T" in string)

# Working with numbers using build in functions and math module

print(round(3.265))


print(math.ceil(3.256))
print(math.floor(3.265))

# Getting input from user

answer = input("Please Enter a number to be doubled >...")  # Returns a string

# Converting values to different type - if working with numbers from input will need to convert value from type string

# int(answer)
# float(answer)
# bool(answer)
# str(answer)  # For converting to a string

x = int(answer) * 2

print(f"Here is you answer doubled..{x}")

# if Statements

number_of_drivers = 10
number_vehicles = 8

if number_of_drivers > number_vehicles:  # Needs to end with a colon
    print("You have spare drivers!")
print("This will be printed regardless as it is outside the if statement")

# elif can be used to add multiple conditions to a if statement

age = 16
height = 6

if age > 18:
    print("You are old enough to enter")
elif height < 5:
    print("You are too small")
else:
    print("This will be done if all conditions arnt met")

# if statements using ternery operator for cleaner code

cost = 100

message = "This is expensive" if cost >= 100 else "This is affordable"
print(message)

# Logical Opertators and / or / not

check_1 = True
check_2 = True
test_1 = False
if check_1 and check_2:
    print("Do something")
else:
    print("Dont do anything")

# with 'and' operator both conditions must be true with 'or' only one condition needs to be true

# not operator reverses the value of the boolean

if (check_1 or check_2) and not test_1:
    print("This works")

# for loops for repeating tasks

for x in range(5):
    print("Result!")

# This loop will run from 1 - 10 times in steps of 2. It also prints the loop number each time to the screen

for x in range(1, 10, 2):

    print("New result!", x)

# for else loops - this for loop contains a if statement so will run through the loop 3 times unless condition is mend in which case it breaks out

valid = True

for x in range(3):
    print("Attempt")
    if valid:
        print("Test is Valid")
        break
else:                               # adding the else allows instructions for the case of the for loop running 3 times and the condition not being met
    print("Unsucessful")

# nested loops

for x in range(10):                # in this nested loop z will run 3 times for every time x is ran
    for z in range(3):
        print(f"{x},{z}")

# while loops are used to repeat something while a condition is true

number = 2

while number > 100:
    print(number)
    number = number * 2
    number *= 2             # this is a shorter way of writing the above line
