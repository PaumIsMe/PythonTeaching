# <---- TYPES OF LINES OF CODE ---->

# Assignments [any code that sets a variable, almost always contains =]
# Ex:

q = 6
x = "Fox"
t = q - 2
u = 9
u = u + 1

# Functions
# Ex:

print("Hewwo")
max(3, 4) # <- Note this code doesn't do anything, it finds the max of 3 and 4 and then throws it to the wind cause we don't assign or print it

# Control Flow [Decides what part of the code we run / don't run / run multiple times]
# Ex:

if u == q + t:
    print("Hehehe, qt")
else:
    print("Butt")

for i in range(10):
    print(i)

while (q < 10):
    print(q)
    q = q + 1




# <----- OPERATIONS ---->

# // -> devides and rounds down
x = 77 // 10 # results in 7

# % -> devides and takes the remainder
x = 9 % 2 # results in 1




# <------ LISTS ----->

# A list/array is a list of values in some order
arr = [3, 6, 2, 9, 10, 33]
arr = []
arr = ["Hello", "I", "am", "a", "stupid", x]

# Get an element from an array
elem = arr[1]

# Change an element of an array
arr[4] = "cute"

# Get length of an array
array_length = len(arr)

# Add an element to the array
arr.append("uwu")

# Remove an element from the array (this removes the first instance of this element)

arr.remove("cute") #This removes the first instance of the word 'cute'
arr.pop(0) #This removes the first element (index 0)

# Enumerate - a short hand for going through every element in a for loop as well as it's index

for i in range(0, len(arr)):
    my_element = arr[i]
    print("This list contains ", my_element, " at position ", i)

#This is equivalent to

for i, my_element in enumerate(arr):
    print("This list contains ", my_element, " at position ", i)


# <---- DICTIONARY ---->

# Used for storing unordered data where we need to find a specific element, and/or mapping elements to values
my_dictionary = {"Bob": 13, "Lisa": 72, "Jerry": 54, "John": 54}

# Sets are like dictionaries, but the entries don't map to anything. Useful for checking if something is in a set
my_set = {"Bob", "Lisa", "Jerry"}

# Add and remove from a set
my_set.add("Larry")
my_set.remove("Larry")

# Adding an element to a dictionary
my_dictionary["New Student"] = 99

# Removing an element from a dictionary
my_dictionary.pop("Bob")

# Changing an element in a dictionary
my_dictionary["Lisa"] = 54

# Getting a list of all the keys/values from a dictionary
key_list = list(my_dictionary.keys())
value_list = list(my_dictionary.values())

# Check to see if a dictionary has an element
new_student_test = "New Student" in my_dictionary
print("Do I have a new student? ", new_student_test)


# <----- RANGES ----->

# 1-input Range
# -> goes from the 0 to the number (exclusive)
x = range(10) # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2-input Range
# -> goes from the first number(inclusive) to the last number (exclusive)
x = range(5, 10) # -> [5, 6, 7, 8, 9]

# 3-input Range
# -> goes from the first number (inclusive) to the second number (exclusive)
x = range(4, 38, 10) # -> [4, 14, 24, 34]

# Range that goes from 0 to 10, every other element
x = range(0, 10, 2)




# <----- LOOPS ----->

# while loop - Runs indefinitely but only WHILE the condition evaluates to True
x = 3
while(x >= 0):
    print(x)
    x = x - 1

# for Loop - Runs once for each element in a list, range, set, ... any iterable object
for i in arr:
    print(i)

# Range - a quick way to make list. Starts at 0 up to and EXCLUDING the number you give it
my_range = range(10)
print(list(my_range)) # Ignore the 'list()' in here, just pretend we're printing my_range. For our purposes it's the same




# <----- FUNCTIONS ------>

# Makes code re-usable, more readable, allows partitioning of workload

#Writing a function
def function_name(function_input1, function_input2, function_input3, etc):
    # Write code here to process inputs
    result_the_function_got = 100000
    return result_the_function_got

#Calling a function
answer = function_name(0, 16, 800, "Harry Potter")

print("Hello world") # 'print' is the function name that you're calling, "Hello world" is the input to the function




# <----- EXAMPLES ----->

# Print every element in an array:
arr = [3, 6, 2, 9, 10, 33]

for elem in arr:
    print(elem)

# Sum every element in an array
arr = [3, 6, 2, 9, 10, 33]

sum = 0

for num in arr:
    sum = sum + num

print(sum)

# Set EVERY element of the array to 0 [hint, loops]
arr = [3, 6, 2, 9, 10, 33]

for i in range(len(arr)):
    arr[i] = 0

print(arr)

# Function to sum all elements in array
def sum_array(arr):

    sum = 0

    for num in arr:
        sum = sum + num
    
    return sum
