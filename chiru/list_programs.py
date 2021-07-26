# Find the second largest elements

a = []
n = int(input("Enter number of elements:"))
for i in range(1, n + 1):
    b = int(input("Enter int element:"))
    a.append(b)
a.sort()
print("Second largest element is:", a[n - 2])


# Swap function

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


# NewList details
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# removing duplicated from list
# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

# to remove duplicated from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
        
# printing list after removal
print("The list after removing duplicates : " + str(res))

# Python Program to read a list of words and return the length of the longest one
a = []
n = int(input("Enter the number of elements in list:"))
for x in range(0, n):
    element = input("Enter str element" + str(x + 1) + ":")
    a.append(element)
max1 = len(a[0])
temp = a[0]
for i in a:
    if (len(i) > max1):
        max1 = len(i)
        temp = i
print("The word with the longest length is:" + temp)
