# Print "Hello World"
print("Hello World")

# Conditional statement: If 5 is greater than 2, print "yes"
if 5 > 2:
    print("yes")  # Proper indentation is necessary in Python

# This is a single-line comment

"""
This is a multiline comment.
It can span multiple lines.
"""

# Assigning a string value "Volvo" to the variable carname
carname = "Volvo"

# Assigning a value of 50 to the variable x, then changing it to 5
x = 50
x = 5

# Assigning a value of 10 to the variable y
y = 10

# Adding x and y and printing the result (5 + 10)
print(x + y)

# Reassigning x and y to 5 and 10 respectively, then adding them to get z
x = 5
y = 10          
z = x + y
print(z)  # This prints 15

# Assigning the same value (tuple) to x, y, and z
x = y = z = ("orange", "banana", "cherry")

# Insert the correct syntax to assign the same value "banana" to x, y, and z
x = y = z = "banana"

# Using the 'global' keyword to declare x as a global variable within a function
def myfunc():
    global x
    x = "fantastic"

# Check the data type of x, which is currently an integer
x = 5
print(type(x))  # This prints <class 'int'>

# Check the data type of x, which is now a string
x = "Hello World"
print(type(x))  # This prints <class 'str'>

# Check the data type of x, which is now a float
x = 20.5
print(type(x))  # This prints <class 'float'>

# Check the data type of x, which is now a list
x = ["apple", "banana", "cherry"]
print(type(x))  # This prints <class 'list'>

# Check the data type of x, which is now a tuple
x = ("apple", "banana", "cherry")
print(type(x))  # This prints <class 'tuple'>

# Check the data type of x, which is now a dictionary
x = {"name": "John", "age": 36}
print(type(x))  # This prints <class 'dict'>

# Check the data type of x, which is now a boolean
x = True
print(type(x))  # This prints <class 'bool'>

# Convert x to a floating-point number
x = 5
x = float(x)

# Convert x to an integer
x = 5.5
x = int(x)

# Convert x to a complex number
x = 5
x = complex(x)

# Use the len function to print the length of the string "Hello World"
x = "Hello World"
print(len(x))  # This prints 11

# Get the first character of the string txt
txt = "Hello World"
x = txt[0]  # This gets 'H'

# Get the characters from index 2 to index 4 (inclusive of start, exclusive of end)
txt = "Hello World"
x = txt[1:5]  # This gets 'ello'

# Return the string without any whitespace at the beginning or the end
txt = " Hello World "
x = txt.strip()  # This removes the leading and trailing spaces
print(x)

# Convert the value of txt to upper case
txt = "Hello World"
txt = txt.upper()  # Converts to "HELLO WORLD"

# Convert the value of txt to lower case
txt = "Hello World"
txt = txt.lower()  # Converts to "hello world"

# Replace the character H with a J in the string
txt = "Hello World"
txt = txt.replace("H", "J")  # Converts to "Jello World"

# Insert the correct syntax to add a placeholder for the age parameter in the string
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # This prints "My name is John, and I am 36"

# The following statement checks if 10 is greater than 9 and prints the result (Boolean value)
print(10 > 9)  # This prints True

# The following statement checks if 10 is equal to 9 and prints the result (Boolean value)
print(10 == 9)  # This prints False

# The following statement checks if 10 is less than 9 and prints the result (Boolean value)
print(10 < 9)  # This prints False

# The following statement checks if the string "abc" is truthy and prints the result (Boolean value)
print(bool("abc"))  # This prints True

# The following statement checks if the integer 0 is truthy and prints the result (Boolean value)
print(bool(0))  # This prints False

# Multiply 10 by 5 and print the result
print(10 * 5)  # This prints 50

# Divide 10 by 2 and print the result
print(10 / 2)  # This prints 5.0

# Use the correct membership operator to check if "apple" is present in the fruits object
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")  # This prints if "apple" is in the list

# Use the correct comparison operator to check if 5 is not equal to 10
if 5 != 10:
    print("5 and 10 are not equal")  # This prints if the condition is true

# Use the correct logical operator to check if at least one of two statements is True
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")  # This prints since the second condition is true

# Print the second item in the fruits list
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # This prints "banana"

# Change the value from "apple" to "kiwi" in the fruits list
fruits[0] = "kiwi"  # Now fruits is ["kiwi", "banana", "cherry"]

# Use the append method to add "orange" to the fruits list
fruits.append("orange")  # Now fruits is ["kiwi", "banana", "cherry", "orange"]

# Use the insert method to add "lemon" as the second item in the fruits list
fruits.insert(1, "lemon")  # Now fruits is ["kiwi", "lemon", "banana", "cherry", "orange"]

# Use the remove method to remove "banana" from the fruits list
fruits.remove("banana")  # Now fruits is ["kiwi", "lemon", "cherry", "orange"]

# Use negative indexing to print the last item in the list
print(fruits[-1])  # This prints "orange"

# Use a range of indexes to print the third, fourth, and fifth items in the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  # This prints ['cherry', 'orange', 'kiwi']

# Print the number of items in the fruits list
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # This prints 3

# Use the update method to add items from more_fruits to the fruits set
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)  # Now fruits is {"apple", "banana", "cherry", "orange", "mango", "grapes"}
