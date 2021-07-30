#-	Create a class which performs basic calculator operations
import sys
class basiccalculator:
    @staticmethod
    def addition(a,b):
        print("The addition of 2 numbers in calculator is ::",a + b)

    @staticmethod
    def subtraction(a,b):
        print("The subtraction of 2 numbers in calculator is ::",a - b)

    @staticmethod
    def multiplication(a,b):
        print("The multiplication of 2 numbers in calculator is ::",a * b)

    @staticmethod
    def division(a,b):
        print("The division of 2 numbers in calculator is ::",a / b)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
X = basiccalculator()
choice = 0
while True:
    print("0. ADDITION")
    print("1. SUBTRACTION")
    print("2. MULTIPLICATION")
    print("3. DIVISION")
    choice = int(input("Enter your choice:"))
    if choice == 0:
        print(X.addition(a,b))
    elif choice == 1:
        print(X.subtraction(a,b))
    elif choice == 2:
        print(X.multiplication(a,b))
    elif choice == 3:
        print(X.division(a,b))
    else:
        print("Invalid choice")
        sys.exit()