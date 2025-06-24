from app import BaseModel


class ExamCreate(BaseModel):
    student_id: int
    number: int
    
class ExamResponse(BaseModel):
    id: int
    student_id: int
    number: int