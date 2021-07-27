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

#swaping the first and last value
Lst=[]
x=int(input("enter the lenght of list:::"))
for i in range(x):
    n=int(input("Enter the value::"))
    Lst.append(n)
print(Lst)
Lst[0],Lst[-1]=Lst[-1],Lst[0]
print(Lst)

#Remove the duplicate items from the list
Lst=[]
x=int(input("enter the lenght of list:::"))
for i in range(x):
    n=int(input("Enter the value::"))
    Lst.append(n)
print ("The original list is : ",Lst)
NewLst=[]
for n in Lst:
    if n not in NewLst:
        NewLst.append(n)
print("The list after removing duplicates:",NewLst)

#-	read a list of words and return the length of the longest one


Lst=[]
x=int(input("enter the lenght of list:::"))
for i in range(x):
    n=str(input("Enter the value::"))
    Lst.append(n)
print(Lst)

Long=len(Lst[0])
for x in Lst:
    if len(x)>Long:
        Long=len(x)
print("Print the length of longest word in the list is ",Long)