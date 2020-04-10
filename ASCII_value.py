# Program to find the ASCII value of the given character
#Here we have used ord() function to convert a character to an integer (ASCII value). 
#This function returns the Unicode code point of that character.
#ord() is a built-in function

value = (input("Enter the character: "))
print("The ASCII value of ' " + value + " ' is", ord(value))