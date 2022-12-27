arr = [6, 2, 3, 5]

# Function to sum every element
def sum_array(arr):

    sum = 0

    for num in arr:
        sum = sum + num
    
    return sum

# This is not

print("Hello") # print is the function name, "Hello" is the input
sum_of_array = sum_array(arr)
print(sum_of_array)