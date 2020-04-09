#program to make a simple calculator using functions in python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

print("Menu:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE\n")

choice = int(input("Enter a choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print(a, "+", b,"=", add(a, b))

elif choice == 2:
    print(a, "-", b, "=", subtract(a,b))

elif choice == 3:
    print(a, "*", b, "=", multiply(a,b))

elif choice == 4:
    print(a, "/", b, "=", divide(a,b))