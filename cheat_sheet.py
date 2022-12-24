# <---- TYPES OF LINES OF CODE ---->

# Assignments [any code that sets a variable, almost always contains =]
# Ex:

q = 6
x = "Fox"
t = q - 2
u = 9
u = u + 1

# Functions [We will learn later...for now think of it as magic code that does something for you]
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

arr.remove(33) #This removes the first instance of element 33
del arr[0] #This removes the first element (index 0)




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
