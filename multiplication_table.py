# Multiplication table (from 1 to 10) in Python

#Can declare number already
#num = 12

#Or To take input from the user
num = int(input("Enter a number: "))
print("Mulitplication table of {} is: " .format(num))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)