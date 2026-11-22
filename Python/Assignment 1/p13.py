# 13. Write a python program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday.
# Test Data
# Input number: 3
# Expected Output :
# Wednesday

a = int(input("Enter a choice between 1-7: "))

if a == 1:
    print("Monday")
elif a == 2:
    print("Tuesday")
elif a == 3:
    print("Wednesday")
elif a == 4:
    print("Thursday")
elif a == 5:
    print("Friday")
elif a == 6:
    print("Saturday")
elif a == 7:
    print("Sunday")