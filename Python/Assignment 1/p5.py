# 5.Take input of age of 3 people by user and determine oldest and youngest among them.

a = int(input("Enter age of 1st p: "))
b = int(input("Enter age of 2nd p: "))
c = int(input("Enter age of 3rd p: "))

if a>b and a>c:
    print("1st person is oldest")
elif b>a and b>c:
    print("2nd person is oldest")
else:
    print("3rd person is oldest")

if a<b and a<c:
    print("1st person is youngest")
elif b<a and b<c:
    print("2nd person is youngest")
else:
    print("3rd person is youngest")
