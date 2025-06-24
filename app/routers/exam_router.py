from fastapi import APIRouter
from app.services.exam_service import ExamService
from app.schemas.exam_schema import ExamCreate

router = APIRouter()

@router.get("/")
async def run():
    return {"message": "exam is running"}

@router.post("/create/")
async def create(data: ExamCreate):
    service = ExamService()
    response = service.CreateExam(data.dict())
    return response

@router.get("/list/")
async def list_exams():
    service = ExamService()
    response = service.ListExam()
    return response

@router.delete("/delete/{id}")
async def delete(id: int):
    service = ExamService()
    response = service.DeleteExam(id)
    return response