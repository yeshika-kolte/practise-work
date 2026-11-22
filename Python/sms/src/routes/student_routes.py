from fastapi import APIRouter, Depends

from src.dependency.dependency import get_student_service
from src.schema.student_schema import StudentRequest
from src.services import student_service
from src.services.student_service import StudentService

router = APIRouter(prefix="/student",tags=["Student"])

@router.post("/")
async def add_student(request:StudentRequest,student_service:StudentService=Depends(get_student_service)):
    student = await student_service.add_student(request)
    return student


@router.get("/")
async def get_all_students(student_service:StudentService=Depends(get_student_service)):
    students = await student_service.get_all_student()
    return students

@router.get("/{id}")
async def get_student_by_id(id:int,student_service:StudentService=Depends(get_student_service)):
    student = await student_service.get_student_by_id(id)
    return student

@router.put("/{id}")
async def update_student(id:int,request:StudentRequest,student_service:StudentService=Depends(get_student_service)):
    student = await student_service.update_student(id,request)
    return student

@router.delete("/{id}")
async def delete_student(id:int,student_service:StudentService=Depends(get_student_service)):
    student = await student_service.delete_student(id)
    return student