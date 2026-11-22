from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import session

from src.model.employee import Employee
from src.db.dbConfig import SessionLocal

class EmployeeDAO:
    @staticmethod
    def save(emp):
        session = None
        try:
            with SessionLocal() as session:
                session.add(emp)
                session.commit()
                return True
        except SQLAlchemyError as e:
            if session:
                session.rollback()
            print(e)
            return False

    @staticmethod
    def get_by_id(id):
        try:
            with SessionLocal() as session:
                emp_id =session.get(Employee, id)
                return emp_id
        except SQLAlchemyError as e:
            print(e)

            