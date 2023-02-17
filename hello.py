
# Lisa got an 82 on the test
# Bob got a 40 on the test
# Jerry got a 91 on the test

my_list = [["Lisa", 82], ["Bob", 40], ["Jerry", 91]]

# What did Lisa get on the test?
# Is Lauren in the class?
# Change Bob's score to a 50 cause he paid me

for entry in my_list:
  if entry[0] == "Lisa":
    print(entry[1])

# Dictionary = Hashmap = Map

grades = {"Lisa": 82, "Bob": 40, "Jerry": 91} # This is a hashmap
grades.pop("Lisa")
print(grades)
print(grades.keys())