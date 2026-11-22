from src.dao.employee_dao import EmployeeDAO
from src.db.dbConfig import engine
from src.db.dbConfig import Base
from src.model.employee import Employee

Base.metadata.create_all(engine)

while True:
    print("Press 0 for exit")
    print("Press 1 for add employee")
    print("Press 2 for get by id")

    choice = int(input("Enter choice : "))

    if choice==0:
        break
    elif choice==1:
        name = input("Enter employee name : ")
        salary = float(input("Enter employee salary : "))
        emp = Employee(name=name, salary=salary)
        if EmployeeDAO.save(emp):
            print("Employee saved")
        else:
            print("Employee not saved")
    elif choice==2:
        id = int(input("Enter employee id : "))
        emp = EmployeeDAO.get_by_id(id)
        if emp:
            print(emp)
        else:
            print("Employee not found")