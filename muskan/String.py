
word1="Hi Bangalore"
word2=word1.replace("a","$")
print word2


word3="Hello Bangalore Metro City"
word4=word3.replace(" ","_")
print word4


string = "Hello BangaLORE "

upper, lower = 0, 0
for i in string:
    
    if(i>='a' and i<='z'):
        lower = lower + 1
    elif(i>='A' and i<='Z'):
        upper = upper + 1


print('Lowercase characters:',lower)
print('Uppercase characters:',upper)




def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO, substring is npt present in a given string")
    else:
        print("YES, substring is present in a given string")
            

string = "examples for python"
sub_str ="examples"
check(string, sub_str)


