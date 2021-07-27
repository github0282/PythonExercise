#-	Read a String from the User and Append it into a File
fname = input("Enter file name: ")
#f=open(fname,"w")
f=open(fname,"a")
c=input("Enter string to append: \n");
f.write("\n")
f.write(c)
#f.close()
print("Contents of appended file:");
f=open(fname,'r')
print (f.read())

#-	 Copy the Contents of One File into Another
import shutil
#The shutil.copy() method in Python is used to copy the content of the source file to destination file or directory.

# use copyfile()
shutil.copyfile('first.txt', 'second.txt')

#-	 Read a Text File and Print all the Numbers Present in the Text File
fname = input("Enter file name: ")
f=open(fname,'r')
for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter.isdigit()):
                    print(letter)

#-	 Read a File and Capitalize the First Letter of Every Word in the File
fname = input("Enter file name: ")

f=open(fname,'r')
for line in f:
        l = line.title()
        print(l)