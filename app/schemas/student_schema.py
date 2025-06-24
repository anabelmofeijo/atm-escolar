from app import BaseModel


class StudentCreate(BaseModel):
    name: str
    student_number: int
    password: str
    
class StudentResponse(BaseModel):
    id: int
    name: str
    student_number: int
    password: str