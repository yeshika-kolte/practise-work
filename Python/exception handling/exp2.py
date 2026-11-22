print ("enter the age")

try:
    age=int(input("enter the age of person:"))
    print(f"your age is:{age}")

except ValueError:
    print("unexpected value error")