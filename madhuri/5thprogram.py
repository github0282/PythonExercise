#-	Create a class in which one method accepts a string from the user and another prints it

class A:

    def __init__(self):
        self.string =""

    def get(self):
        self.string = input("Enter string: ")

    def put(self):
        print("String is:",self.string)



refvar = A()
refvar.get()
refvar.put()