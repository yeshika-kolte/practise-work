from pydantic import BaseModel


class StudentRequest(BaseModel):
    name:str
    email:str
    course:str
    age:int