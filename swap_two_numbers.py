#swap two numbers

x = int(input("Enter first number: x= "))
y = int(input("Enter second number: y= "))

print("Value of x and y before swapping is {0} and {1}" .format(x,y))

#swapping using temp 

temp = x
x = y
y = temp

print("\nThe value of x and y after swapping is {0} and {1}" .format(x ,y))