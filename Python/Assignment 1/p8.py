# 8. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

heldClasses = int (input("Enter number of classes held:"))
attendedClasses =int (input("Enter number of classes attended:"))
medical = input("Any medical cause enter Y/N")
percentage = (attendedClasses / heldClasses) *100

print(f"Attendance percentage: {percentage}%")

if medical== "Y" or medical== "y":
    print("Student allowed to sit")
elif percentage >= 75:
    print("Student is allowed to sit in exam.")
else:
    print("Student is not allowed to sit in exam.")