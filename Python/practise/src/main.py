from model.employee import Employee
from dao.employee_dao import EmployeeDAO
while True:
    print("Press 1 for insertion")
    print("Press 2 for fetchall")
    print("Press 3 for update")
    print("Press 4 for delete")
    print("Press 5 for fetch by id")
    print("Press 0 for exit")
    choice=int(input("enter yur choice:"))

    if choice ==1:
        name = input("enter your name:")
        salary = float(input("enter your salary:"))
        department = input("enter your department:")
        emp = Employee(None, name, salary, department)
        if EmployeeDAO.save(emp):
            print("Employee saved")
        else:
            print("Something is not correct")

    elif choice==0:
        break
    elif choice ==2:
        EmployeeDAO.fetch_all()
    elif choice==3:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        department = input("Enter your department: ")
        id = int(input("Enter employee id: "))
        emp = Employee(id,name,salary,department)
        if EmployeeDAO.update(emp) :
            print("Record updated ")
        else:
            print("Something is not correct")  
    elif choice==4:
        id =int(input("enter employee id:"))
        if EmployeeDAO.delete(id):
            print("record deleted")
        else:
            print("something is not correct")
    elif choice ==5:
        id= int(input("enter employee id"))
        EmployeeDAO.find_by_id(id)



