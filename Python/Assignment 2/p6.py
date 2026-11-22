# Write a program using the conditional operator to assign grades based on marks:
# ≥ 90 → A
# ≥ 75 → B
# ≥ 60 → C
# < 60 → Fail

num = int(input("Enter you no: "));
if(num>90):
    print("A")
elif num>75 :
    print("B")
elif num>60:
    print("C")
else:
    print("Fail")