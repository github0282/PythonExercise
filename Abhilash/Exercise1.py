# find the second largest number in a list
list1 = []
num1 = int(input("Enter the number of elements in a list: "))
for i in range(num1):
    data = int(input("Enter element:"))
    list1.append(data)
list1.sort()
print("Second largest element is:", list1[-2])

# swap the first and last value of a list
list2 = []
num2 = int(input("Enter the number of elements in a list: "))
for i in range(num2):
    data = int(input("Enter element:"))
    list2.append(data)
print("First number is:",list2[0])
print("Last number is:", list2[-1])

temp = list2[0]
list2[0] = list2[-1]
list2[-1] = temp

print("After swap, First number is:",list2[0])
print("After swap, Last number is:", list2[-1])

# remove the duplicate items from the list
list3 = []
num3 = int(input("Enter the number of elements in a list: "))
for i in range(num3):
    data = int(input("Enter element:"))
    list3.append(data)

print(list3)
list3 = set(list3)
print("After removing duplicates:",list(list3))

# read a list of words and return the length of the longest one
list4=[]
num4= int(input("Enter the length of the list:"))
for i in range(num4):
    data = str(input("Enter element:"))
    list4.append(data)

print("The list is:", list4)
length=len(list4[0])
temp=list4[0]

for j in list4:
    if(len(j)>length):
       length=len(j)
       temp=j
print("The word with the longest length is:", temp)
