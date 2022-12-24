# I very much encourage using the cheat sheet to help until you have to syntax memorized, which will come with time
# If you get stuck or something isn't working, step 1 is to try and figure it out yourself, if you feel like you haven't made any progress in 5-10m feel free to ask
# Remember: the arrays given are examples. Your code should work for *any* set of values I put in that array (arr) variable

arr = [-3, 76, -9, 23, 3, 0, 1]

# 1 - print the sum of all the elements in a list

sum = 0
for num in arr:
    sum += num

print(num)

# 2 - Change all negative elements of the array to 0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print(arr)

# 3 - Add a copy of the array to the end of it (i.e. [1, 2, 6] becomes [1, 2, 6, 1, 2, 6])
for i in range(len(arr)):
    arr.append(arr[i])

print(arr)
 
# 4 - Remove every even element from an array
for i in range(len(arr)):
    if i % 2 == 0:
        arr.remove(i)

print(arr)

# 5 - Use the input() command to keep asking a user to type "Yes" until they finally type "Yes"

while(input() != "Yes"):
    print()


arr = [[3, 6, 2], [1, 1, 100], [10, 11]]

# 6 - From the given list of arrays, find the one with the largest product, and print it
largest_a = []
largest_product = -10000

for a in arr:
    product = 1
    for num in arr:
        product *= num
    
    if product > largest_product:
        largest = sum
        a = product

print(largest_a)

# 7 - Remove the shortest array from the list of arrays
shortest_a = []
shortest_len = 100000

for a in arr:
    if len(a) < shortest_len:
        shortest_a = a
        shortest_len = len(a)

a.remove(shortest_a)

# 8 - Turn this array into a single array with 0 between each of the sub-arrays. For example: [[3, 6, 2], [1, 1, 100], [10, 11]] becomes [3, 6, 2, 0, 1, 1, 100, 0 10, 11]
new_array = []

for a in arr:
    new_array.append(0)
    for elem in a:
        new_array.append(elem)
    
new_array = new_array.remove(0)