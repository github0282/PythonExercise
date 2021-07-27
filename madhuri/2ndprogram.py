#replace all occurrences of ‘a’ with $ in a String
Line=input("enter any sentence:")
print("Replaced letter a in sentence with $ symbol::::",Line.replace("a","$"))

#Take a string and replace every blank space with hyphen
print("Replaced blank space with hypen::::",Line.replace(" ","-"))


###count the number of upper case and lower-case letters in a string###
Line=input("enter any sentence:")
Lower=0
Upper=0
for x in Line:
    if (x.islower()):
        Lower+=1
    elif(x.isupper()):
         Upper+=1
print("The lower case letters::",Lower)
print("The upper case letters::",Upper)

##-	Check if a substring is present in a given string
import re

Str=input("enter the string::")
i=input("enter the substring::")
if re.search(i,Str):
    print("yes the substring is present::",i)
else:
    print("No such substring is present")