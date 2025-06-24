from app.models.exam_model import Exam
from core.config import SessionLocal


class ExamService:
    
    @staticmethod
    def CreateExam(new_data: dict):
        with SessionLocal() as db:
            new_exam = Exam(**new_data)
            db.add(new_exam)
            db.commit()
            db.refresh(new_exam)
            db.close()
            return {"exam-added": new_data}
        
    @staticmethod
    def DeleteExam(id: int):
        with SessionLocal() as db:
            data = db.query(Exam).get(id)
            if data:
                db.delete(data)
                db.commit()
                return {"message": "exam deleted successfully"}
            return {"error": "exam nof found!"}
            
            
    @staticmethod
    def ListExam():
        with SessionLocal() as db:
            data = db.query(Exam).all()
            if data:
                return data
            return {"error": "there is not any exam in db"}