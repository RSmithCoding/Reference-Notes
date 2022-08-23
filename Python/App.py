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
