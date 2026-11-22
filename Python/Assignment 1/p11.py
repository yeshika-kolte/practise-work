# 11. Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

age = int(input("Enter age: "))
gender = input("Enter gender (M or F): ")
marital = input("Enter marital status (Y or N): ")

if age < 20 or age > 60:
    print("Error")
elif gender == 'F' or gender == "f":
    print("urban areas only")
elif gender == 'M' or gender == "m":
    if 20 <= age <= 40:
        print("may work anywhere")
    else:
        print("urban areas only")

