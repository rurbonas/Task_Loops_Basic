# Task 1
# make a loop with a range that says hello 10 times
for i in range(10):
    print("Hello")


# Task 2
# create another loop with a range that asks for names and appends to list names
names = []
num = 0
for i in range(5):
    name = input("add a number to index {} >> ".format(i))
    names.append(name)
print(names)

# Task 3
# make a loop that iterated over each name in list_name and format's it into lowercase in a new variable called list_names_lower
list_name = ["John", 'pEter', 'PRODIGY', 'ricky']
list_names_lower = []
for name in list_name:
    list_names_lower.append(name.lower())
print(list_names_lower)

# #Task 4
#Iterate over the list of values to find if they are even
names = ["John", 'pEter', 'PRODIGY', 'ricky']
for name in names:
    if len(name) % 2 == 0:
        print("{}, has an even number of letters".format(name))
    else:
        print("{}, has an odd number of letters".format(name))

if len(names) % 2 == 0:
    print("List {}, has an even number of items".format(names))
else:
    print("List {}, has an odd number of items".format(names))
