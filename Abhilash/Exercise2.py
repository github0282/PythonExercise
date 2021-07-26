# replace all occurrences of ‘a’ with $ in a String

text1 = str(input("Enter a string: "))
print("The string is:", text1)
search = text1.find("a")
if(search == -1):
    print("Character a not present in string")
else:
    text1 = text1.replace("a","$")
    print(text1)

# Take a string and replace every blank space with hyphen
text2 = str(input("Enter a string: "))
print("The string is:", text2)
text2 = text2.replace(" ","-")
print(text2)

# count the number of upper case and lower-case letters in a string
text3 = str(input("Enter a desired string: "))
print(text3)

UpperCase = 0
LowerCase = 0

for i in text3:
    if( i >= "a" and i <= "z"):
        LowerCase = LowerCase + 1
    if( i >= "A" and i <= "Z"):
        UpperCase = UpperCase + 1

print("No of UpperCase Characters: ", UpperCase)
print("No of LowerCase Characters: ", LowerCase)

# Check if a substring is present in a given string
text4 = str(input("Enter a desired string: "))
substring = str(input("Enter the substring: "))

if(text4.find(substring) == -1):
    print("Substring is not present in the string")
else:
    print("Substring is present in the string")