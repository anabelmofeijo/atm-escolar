from fastapi import APIRouter
from app.schemas.student_schema import StudentCreate
from app.services.student_service import StudentService

router = APIRouter()

@router.get("/")
async def run():
    return {"message": "student is running"}

@router.post("/create/")
async def create_student(data: StudentCreate):
    service = StudentService()
    response = service.CreateStudent(new_data=data.dict())
    return response

@router.get("/find/{student_number}")
async def find_student_by_id(student_number: int):
    service = StudentService()
    response = service.FindStudent(student_number)
    return response

@router.get("/list-all/")
async def list_all_students():
    service = StudentService()
    response = service.ListStudent()
    return response

@router.delete("/delete/{id}")
async def delete_student(id: int):
    service = StudentService()
    response = service.DeleteStudent(id)
    return response