from app.models.student_model import Student
from app.core.config import SessionLocal


class StudentService:
    
    @staticmethod
    def CreateStudent(new_data: dict):
        with SessionLocal() as db:
            new_student = Student(**new_data)
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            db.close()
            return {"new_student": new_data}
        
    @staticmethod
    def DeleteStudent(id: int):
        with SessionLocal() as db:
            data = db.query(Student).get(id)
            if data:
                db.delete(data)
                db.commit()
                return {"message": "student deleted successfully"}
            return {"error": "student not found"}
        
    @staticmethod
    def ListStudent():
        with SessionLocal() as db:
            data = db.query(Student).all()
            if data:
                return data
            return {"erro": "there is not any student in database"}
        
    @staticmethod
    def FindStudent(student_number: int):
        with SessionLocal() as db:
            data = db.query(Student).filter(Student.student_number == student_number).first()
            if data:
                return data
            return {"error": "user not found"}