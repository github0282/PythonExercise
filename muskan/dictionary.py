dic1={'A':1,'B':2}
print("The first dictionary is :", dic1)
dic2={'C':3,'D':4}
print("The first dictionary is :", dic2)
dic1.update(dic2)
print("Concatenated dictionary is:")
print(dic1)
print (" ")

myDict = {'a':1,'b':2,'c':3,'d':4}
print("My dictionary" ,myDict)
if 'b' in myDict: 
    del myDict['b']
print("the dictionary after key removal" ,myDict)
print (" ")

keys = ["Roy", "Tim", "Volt"]
values = [31,14,25]
Name_age_dictionary = dict(zip(keys, values))
print("Name_age_dictionary is :" ,Name_age_dictionary)
print (" ")

my_string = "Hello World Hello earth hi World"
print("the actual statement is:" , my_string)
my_list=[]
my_list=my_string.split()
word_freq=[my_list.count(p) for p in my_list]
print("The frequency of words is ...")
print(dict(zip(my_list,word_freq)))

