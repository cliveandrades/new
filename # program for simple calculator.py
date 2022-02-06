# program for simple calculator
from random import choice


print("Welcome to simple caculator")

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("enter the choice of number for suitable operation.")
print("1 for addition")
print("2 for subtration.")
print("3 for multiplication.")
print("4 for division.")


while True:
    choice = input("Enter your choice 1/2/3/4: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
