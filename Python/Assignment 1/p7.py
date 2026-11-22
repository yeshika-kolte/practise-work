# 7. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not

heldClasses = int (input("Enter number of classes held:"))
attendedClasses =int (input("Enter number of classes attended:"))
percentage = (attendedClasses / heldClasses) *100

print(f"Attendance percentage: {percentage}%")

if percentage >= 75:
    print("Student is allowed to sit in exam.")
else:
    print("Student is not allowed to sit in exam.")