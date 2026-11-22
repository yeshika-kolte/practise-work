import json

def load_data():
    with open("emp.json","r") as f:
        data = json.load(f)
        return data

def save_data(data):
     with open("emp.json", "w") as file:
        json.dump(data, file, indent=4)

def insert():
    data = load_data()
    emp = {}

    emp["id"]: input("Enter ID: ")
    emp["name"]: input("Enter Name: ")
    emp["salary"]: input("Enter Salary: ")

    data.append(emp)
    save_data(data)
    print("Employee Added ")

def select_all():
    data = load_data()

    if len(data) == 0:
        print("No Records Found")
        return

    for emp in data:
        print(f"ID : {emp['id']}")
        print(f"Name : {emp['name']}")
        print(f"Salary : {emp['salary']}")

def select_by_id():
    search_id = input("Enter Employee ID: ")
    data = load_data()

    for emp in data:
        if emp["id"] == search_id:
            print("Employee Found")
            print(emp)
            return

    print("Employee Not Found")

def search_by_name():
    search_name = input("Enter Name: ")
    data = load_data()
    found = False

    for emp in data:
        if search_name in emp["name"].lower():
            print(emp)
            found = True

    if not found:
        print("Employee Not Found")

def update_employee():
    search_id = input("Enter Employee ID: ")
    data = load_data()
    found = False

    for emp in data:
        if emp["id"] == search_id:
            emp["name"] = input("Enter New Name: ")
            emp["salary"] = input("Enter New Salary: ")
            found = True
            break

    save_data(data)
    if found:
        print("Employee Updated Successfully")
    else:
        print("Employee Not Found")

def delete_employee():
    search_id = input("Enter Employee ID: ")
    data = load_data()
    new_data = []
    found = False

    for emp in data:
        if emp["id"] == search_id:
            found = True
        else:
            new_data.append(emp)

    save_data(new_data)
    if found:
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")


while True:

    print(" ")
    print("Enter 1 for Creating New Emp")
    print("Enter 2 to view all emp")
    print("Enter 3 to view emp by id")
    print("Enter 4 to update emp")
    print("Enter 5 to delete emp")
    print("Enter 6 to search emp by name")
    print("Enter 7 to exit")
    print(" ")

    choice = input("Enter Choice: ")
    print(" ")

    if choice == "1":
        insert()

    elif choice == "2":
        select_all()

    elif choice == "3":
        select_by_id()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        search_by_name()

    elif choice == "7":
        break

    else:
        print("Invalid Choice")