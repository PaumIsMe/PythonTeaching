# 1 - return the sum of all the elements in a list
def sum_all_elems(arr : list):
    sum = 0
    for num in arr:
        sum += num
    return sum

# 2 - Change all negative elements of the array to 0
def make_negatives_0(arr : list):
    for i, num in enumerate(arr):
        if num < 0:
            arr[i] = 0
    return arr

# 3 - Add a copy of the array to the end of it (i.e. [1, 2, 6] becomes [1, 2, 6, 1, 2, 6])
def add_array_copy(arr : list):
    for i in range(len(arr)):
        arr.append(arr[i])
    return arr

# 4 - Remove every even element from an array
def remove_even(arr : list):
    new_arr = []
    for i in range(1, len(arr), 2):
        new_arr.append(arr[i])
    return new_arr

# 5 - Use the input() command to keep asking a user to type "Yes" until they finally type "Yes"
def make_user_comply():
    user_input = ""
    while(user_input != "Yes"):
        user_input = input()
    return user_input

# 6 - From the given list of arrays, find the one with the largest product, and return it
def arr_with_largest_product(arr : list):
    largest_prod = 0
    largest_arr = []

    for a in arr:
        prod = 1
        for elem in a:
            prod *= elem
        if prod > largest_prod:
            largest_prod = prod
            largest_arr = a

    return largest_arr

# 7 - Remove the shortest array from the list of arrays
def remove_shortest(arr : list):
    shortest_len = 1000
    shortest_idx = -1

    for i, a in enumerate(arr):
        
        if len(a) < shortest_len:
            shortest_len = len(a)
            shortest_idx = i
    
    arr.pop(shortest_idx)

    return arr

# 8 - Turn this array into a single array with 0 between each of the sub-arrays. For example: [[3, 6, 2], [1, 1, 100], [10, 11]] becomes [3, 6, 2, 0, 1, 1, 100, 0 10, 11]
def concat_double_array(arr : list):
    new_arr = []

    for a in arr:
        for elem in a:
            new_arr.append(elem)
        new_arr.append(0)

    print(new_arr)
    return new_arr[0:-1]

# These assert statements are making sure your functions work as directed. Once you don't have any assertion errors, you (probably) have completed all of the problems
assert [1, 2] == [1, 2], "Logic is dead"
assert sum_all_elems([0, 6, 2, 5, 9, 10, 2, 2]) == 36, "Sum all elems not working"
assert make_negatives_0([0, -6, 2, 5, -9, 10, 2, 2]) == [0, 0, 2, 5, 0, 10, 2, 2], "Make Negatives not working"
assert add_array_copy([0, 6, 2, 5, 9, 10, 2, 2]) == [0, 6, 2, 5, 9, 10, 2, 2, 0, 6, 2, 5, 9, 10, 2, 2], "Add array copy not working"
assert remove_even([0, 6, 2, 5, 9, 10, 2, 2]) == [6, 5, 10, 2], "Remove Even not working"
assert make_user_comply() == 'Yes', "Make user comply not working"
assert arr_with_largest_product([[3, 6, 2], [1, 1, 100], [10, 11]]) == [10, 11], "Array with largest product not working"
assert remove_shortest([[3, 6, 2], [1, 1, 100], [10, 11]]) == [[3, 6, 2], [1, 1, 100]], "Remove shortest not working"
assert concat_double_array([[3, 6, 2], [1, 1, 100], [10, 11]]) == [3, 6, 2, 0, 1, 1, 100, 0, 10, 11], "Concat double array not working"