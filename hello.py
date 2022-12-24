x   = 10                # Statement
y   = "I am a string"   # Statement
Evo = "fox"             # Statement
age = 80                # Statement

# statements assigning VALUES to VARIABLES
# conditionals (control flow)

# bet = 100 # Statement
# guess = 50 # Statement
# correct_guess = 3 # Statement
# result = None # Statement

# if (guess == correct_guess): # conditionals (control flow)
#     result =  bet * 5 # Statement
# else: # conditionals (control flow)
#     result = 0 # Statement

# num = -9

# if num < 0:
#     print(num * -1)
# else:
#     print(num)

# abs(num)

num = 12

# Print all the integers up to 100, [not including 100]
# starting at 40

# range(a, b, c)

# a -> starting value
# b -> upper value (exclusive)
# c -> 'step'

salaries = [100, 500, 300, 73, 23, 36, 2, 3, 1, 2, 46]

# Print first element of list
print(salaries[0])

# Length of the list
print(len(salaries))

# Print all elements of the list
for i in range(len(salaries)):
    print(salaries[i])

# Print the last element of the list:
print(salaries[len(salaries) - 1])
print(salaries[-1])

# Add a value to our list
salaries.append(50)
print(salaries)

# Change the third value of our list to 10
salaries[2] = 10
print(salaries)


salaries = [100, 500, 300, 73, 23, 36, 2, 3, 1, 2, 46]

# Sum of a list

sum = 0

for salary in salaries:
    sum = sum + salary

print(sum)


    
    