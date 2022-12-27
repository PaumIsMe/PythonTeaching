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

print(list(x)) # pretend this is print x