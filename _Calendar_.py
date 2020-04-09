# Program to display calendar of the given month and year

# importing calendar module
import calendar
print("***************     PYTHON CALENDAR     ******************")
#we can declare year or month 
#yy = 2020
#mm = 4
ans = 'yes'
# To take month and year input from the user
while ans: 
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))
    print("\n")
    # display the calendar
    print(calendar.month(yy,mm))

    answer = input("Do You Want TO Continue?(Yes/No) ")

    if answer == 'no':
        break