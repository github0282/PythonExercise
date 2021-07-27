#-	Concatenate two dictionaries into one
dic={}
Dic1={}
keys=[]
values=[]
val=int(input("enter the value:"))
for i in range(val):
    n=input("enter the key:")
    keys.append(n)
    x=input("enter the value:")
    values.append(x)
    dic=dict(zip(keys,values))
print("the first dictionary keys&values are::",dic)
keys1=[]
values1=[]
val=int(input("enter the value:"))
for i in range(val):
    n1=input("enter the key:")
    keys1.append(n1)
    x1=input("enter the value:")
    values1.append(x1)
    Dic1=dict(zip(keys1,values1))
print("the second dictionary keys&values are::",Dic1)
dic.update(Dic1)
print("The concatenated dictionary is::",dic)

#-	Remove the given key from a dictionary
Val1=input("enter the key:")
if Val1 in dic:
    dic.pop(Val1)
    print(dic)
else:
    print("No such key in dictionary")

#-	Map Two lists into a dictionary
dic={}
keys=[]
values=[]
val=int(input("enter the value:"))
for i in range(val):
    n=input("enter the key:")
    keys.append(n)
    x=input("enter the value:")
    values.append(x)
    dic=dict(zip(keys,values))
print("the mapped two lists into dictionary::",dic)

#-	Count the Frequency of words appearing in a string using a dictionary-
mainstring=input("Enter string:")
list=[]
list=mainstring.split()
print("The list of words are:")
print(list)
substringfreq=[list.count(x) for x in list]
freq=dict(zip(list,substringfreq))
print("The substrings frequency in a string:")
print(freq)