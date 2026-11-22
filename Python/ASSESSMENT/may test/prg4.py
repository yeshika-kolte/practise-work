# Question 4 — File Handling (Write and Read)

# Write a Python program to:

# Create a file named student.txt
# Take student details from the user:
# Name
# Course
# Marks
# Store the details into the file.
# Read the file and display the stored data.
# Sample File Content
# Name: Amit
# Course: Python
# Marks: 85

f =open("./student.txt","w")
name=input("enter name:")
course=input("enter course:")
marks=input("enter the marks:")

f.write("Name:"+name+"\n")
f.write("Course:"+course +"\n")
f.write("Marks:"+marks +"\n")
f.close()

f=open("./student.txt","r")
print("store data:")
print(f.read())
f.close()
