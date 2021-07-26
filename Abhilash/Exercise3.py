# Concatenate two dictionaries into one

n = int(input("Enter the number of elements in a dictionary 1: "))
dict1 = {}

for i in range(n):
    key = input("Enter key: ")
    value =  int(input("Enter value: "))
    dict1[key] = value

m = int(input("Enter the number of elements in a dictionary 2: "))
dict2 = {}

for i in range(m):
    key = input("Enter key: ")
    value =  int(input("Enter value: "))
    dict2[key] = value

print("Dictionary 1 is:", dict1)
print("Dictionary 2 is:", dict2)

dict1.update(dict2)
print("The concatenated dictionary is: ",dict1)

# Remove the given key from a dictionary

n = int(input("Enter the number of elements in a dictionary 1: "))
dict3 = {}

for i in range(n):
    key = input("Enter key: ")
    value =  int(input("Enter value: "))
    dict3[key] = value

del_key = input("Enter the key you want to delete: ")

if del_key in dict3:
    del dict3[del_key]
else:
    print("Key is not available")

print("New dictionary is: ", dict3)

# Map Two lists into a dictionary
list1 = []
num1 = int(input("Enter the number of elements in a list: "))
for i in range(num1):
    data = str(input("Enter element:"))
    list1.append(data)

list2 = []
num2 = int(input("Enter the number of elements in a list: "))
for i in range(num2):
    data = int(input("Enter element:"))
    list2.append(data)

dict4 = {}
dict4 = dict(zip(list1,list2))
print("Dictionary created is: ", dict4)

# Count the Frequency of words appearing in a string using a dictionary

text = input("Enter the string of choice: ")
list1 = []
list2 = []
list1 = text.split()
length = len(list1)

for p in list1:
    num = list1.count(p)
    list2.append(num)

dict5 = dict(zip(list1,list2))
print("New Dictionary is:", dict5)
