from fastapi import FastAPI

from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.routes.student_routes import router as student_router
app = FastAPI()

# app.add_exception_handler(ResourceNotFoundException)

app.include_router(student_router)