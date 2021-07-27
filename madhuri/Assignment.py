"""find the second largest number in a list"""

Lst=[]
x=int(input("enter the lenght of list:::"))
for i in range(x):
    n=int(input("Enter the value::"))
    Lst.append(n)
print(Lst)
Lst.sort()
print(Lst)
print("Print the second largest number in the list is ",Lst[-2])