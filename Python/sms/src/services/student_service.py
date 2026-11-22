from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.model import Student
from src.schema.student_schema import StudentRequest


class StudentService:
    def __init__(self,student_repository):
        self.student_repository = student_repository

    async def add_student(self,request:StudentRequest):
        student = Student(name=request.name,email=request.email,course=request.course,age=request.age)
        return await self.student_repository.add_student(student)

    async def get_all_student(self):
        return await self.student_repository.get_all_student()

    async def get_student_by_id(self,id:int):
        return await self.student_repository.get_student_by_id(id)

    async def update_student(self,id:int,request:StudentRequest):
        student = await self.student_repository.get_student_by_id(id)
        if not student:
            raise ResourceNotFoundException("Student not found")
        student.name = request.name
        student.email = request.email
        student.course = request.course
        student.age = request.age

        return student

    async def delete_student(self,id:int):
        return await self.student_repository.delete_student(id)