# 3. WAP to calculate the percentage of students

m1 = float(input("Enter marks of s1: "))
m2 = float(input("Enter marks of s2: "))
m3 = float(input("Enter marks of s3: "))
m4 = float(input("Enter marks of s4: "))
m5 = float(input("Enter marks of s5: "))

total = m1 + m2 + m3 + m4 + m5
maxMarks = 500

percentage = (total / maxMarks) * 100

print("Total Marks =", total)
print("Percentage =", percentage, "%")