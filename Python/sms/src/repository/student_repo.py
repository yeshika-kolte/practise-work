from sqlalchemy import select

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Student


class StudentRepository:
    def __init__(self,session):
        self.session = session

    async def add_student(self,student: Student):
        self.session.add(student)
        await self.session.flush()
        await self.session.refresh(student)
        return student

    async def get_all_student(self):
        stmt = select(Student)
        students = await (self.session.execute(stmt))
        return students.scalars().all()

    async def get_student_by_id(self,id:int):
        student = await self.session.get(Student,id)
        return student

    async def delete_student(self,id:int):
        student = await self.session.get(Student,id)
        if not student:
            raise ResourceNotFoundException("Student not found")
        await self.session.delete(student)
        return student

