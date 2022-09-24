from collections import deque
import math
from os import system

system('cls')

# Printing messages

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

# functions

# defining and calling a function


def welcome():                      # function is defined
    print("Welcome!")


welcome()                           # function is called

# setting parameters and passing arguments to a function


def user_login(first_name, last_name):
    print(f"Welcome; {first_name} {last_name} you are logged in")


user_login("Russell", "Smith")

# writing a function to return a value


def answer(number_1, number_2):
    sum = number_1 + number_2
    return f"Your answer is: {sum}"


new_number = answer(2, 2)

print(new_number)

# passing multiple values into a function which python saves as a dictionary


def character_stats(**stats):
    # this will just out put the strengh value but print(stats) would output the whole dictionary
    print(stats["strength"])


character_stats(name="Russell", strength=58, luck=68)

#   functions have local varibles that cant be called from outside of the function. So functions can share the same varible names

#   lists

#   lists can contain difference object types and can be combined

car_makes = ["Bmw", "Audi", "VW"]
stats = [12, 22, 54, 6]

combined_example = car_makes + stats

two_dimensional_list = [[0, 2], [4, 2]]   # A list of lists

twenty_numbers = list(range(20))    # creates a list of 20 numbers 0-19

# creates a list of the characters in quotes#
characters = list("List of letters")

# length function displays the number of items in the list
print(len(twenty_numbers))

car_makes[2] = "AUDI"   # changes an item in a list

# selects the first item in the list and prints it to the screen
print(stats[0])

print(stats[0:2])

new_stats = stats[0:1]

scores = [2, 56, 78, 4, 6, 8, 23, 46, 73]

for i in scores:        # for loops can be used to go through lists
    print(i)

#   adding and removing from lists

numbers = [34, 56, 23, 56, 756, 32, 5, 1, 7]

numbers.append(46)          # adds something to end of the list
numbers.insert(0, 23)       # adds something to a certain position
numbers.pop(4)              # removes from list based on position
numbers.pop()               # removes from end of list
numbers.remove(23)          # removes first occurance of requested from list

del numbers[0:5]            # removes positions 0-5 from the list

#   finding index of specific item in list

numbers.index(5)

#   checking list for specific item then returning the index

numbers_2 = [1, 4, 6, 3, 76]

if 1 in numbers_2:
    print(numbers_2.index(1))

#   counting how many times something occurs in a list

costs = [2.00, 1.99, 4.50, 4.50, 6.99, 6.50, 4.50]

print(costs.count(4.50))

costs.sort()    # sorts values in asending order, use keyword argument reverse=true to decend list

print(costs)

# sorts in the same way but returns a new list instead of modifying exisitng list
sorted(costs)

direct_debits = [

    ("BT", 4, 21),
    ("PHONE", 3, 1),
    ("RENT", 4, 15)
]


# sorting using lambda when sorting tuples
direct_debits.sort(key=lambda item: item[1])

print(direct_debits)

#   create a new list sorted from the old list only containing the name using the map function

debt_names = list(map(lambda item: item[0], direct_debits))
# cleaner way of writing same as previous line
debt_names_2 = [item[0] for item in direct_debits]
print(debt_names)
print(debt_names_2)

# filtered items into a new list based on a condition
april_debts = list(filter(lambda item: item[1] == 4, direct_debits))
# cleaner way of writing same as previous line
april_debts_2 = [item for item in direct_debits if item[1] == 4]
print(april_debts)
print(april_debts_2)

# used a for loop and formatted string to display list in specific order
for i in direct_debits:
    direct_debits.sort(key=lambda item: (item[1], item[2]))
    print(f"Debit {i[0]} Month {i[1]} Day {i[2]}")

# combining 2 list using zip function

team1_scores = [3, 5, 2, 1]

team2_scores = [2, 3, 3, 5]

print(list(zip("123", team1_scores, team2_scores)))

# stacks (last in first out)

my_score_cards = []             # creates empty list (stack)
print(my_score_cards)
my_score_cards.append(3)        # adds entrys
my_score_cards.append(5)
my_score_cards.append(6)
my_score_cards.append(5)
print(my_score_cards)
my_score_cards.pop()            # deletes the entry at the end of the list
print(my_score_cards)
my_score_cards.pop()
my_score_cards.pop()
my_score_cards.pop()


if not my_score_cards:          # checks to see is stack is empty if false displays last item
    print("Stack empty")
else:
    print(my_score_cards[-1])

#   queues (first in first out)
queue_positiions = deque([])    # creates empty list
queue_positiions.append(3)      # adding items to list
queue_positiions.append(5)
queue_positiions.append(67)
queue_positiions.append(75)
queue_positiions.popleft()      # removes first item
print(queue_positiions)

#   a set is a list of items with no duplicates

#   you can get rid of duplicates from a list by converting to a set

collection = [2, 2, 4, 5, 3, 4, 4, 5, 6, 4, 5, 6, ]

new_collection = set(collection)        # all duplicates are removed

print(new_collection)

other_collection = set([3, 5, 7, 6, 7, 8, 9, 9, 9, ])

# creates a new set with all the items that are in either the first or the second set
print(new_collection | other_collection)
# creates a new set with all the items that are both in the first and the second set
print(new_collection & other_collection)
# creates a new set with all items that are in the first set but not in the second set
print(new_collection - other_collection)
# creates a new set with all items that are in first set and second but not in both
print(new_collection ^ other_collection)
