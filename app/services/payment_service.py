from app.models.payment_model import Payment
from  app.models.monthly_model import MonthlyPayment
from app.core.config import SessionLocal
from app.services.send_email import email
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_pdf = os.path.join(BASE_DIR, "comprovativo.pdf")


class PaymentService:
    
    @staticmethod
    def CreatePayment(new_data: dict):
        with SessionLocal() as db:
            new_data = Payment(**new_data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            email.enviar_comprovativo(destinatario_email="ambrosiozambote@gmail.com", caminho_pdf=caminho_pdf)
            return {"PaymentCreated": new_data}
        
    @staticmethod
    def DeletePayment(id: int): 
        with SessionLocal() as db:
            data = db.query(Payment).get(id)
            if data:
                db.delete(data)
                db.commit()
                return {"message": "payment deleted successfully"}
            return {"error": "there is not any payment in db"}
        
    @staticmethod
    def ListPaymentByStudent(student_id: int):
        with SessionLocal() as db:
            data = db.query(Payment).get(student_id)
            if data:
                return data
            return {"error":"this student is not in db"}
        
    @staticmethod
    def ListPayment():
        with SessionLocal() as db:
            data = db.query(Payment).all()
            if data:
                return data
            return {"error": "there is not any payment in db"}
       
        
class MonthlyPaymentService:
    
    @staticmethod
    def CreatePayment(new_data: dict):
        with SessionLocal() as db:
            new_data = MonthlyPayment(**new_data)
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
            return {"PaymentCreated": new_data}
        
    @staticmethod
    def DeletePayment(id: int):
        with SessionLocal() as db:
            data = db.query(MonthlyPayment).filter(MonthlyPayment.id == id).first()
            if data:
                db.delete(data)
                db.commit()
                return {"message": "payment deleted successfully"}
            return {"error": "there is not any payment in db"}
        
    @staticmethod
    def ListPaymentByStudent(student_id: int):
        with SessionLocal() as db:
            data = db.query(MonthlyPayment).get(student_id)
            if data:
                return data
            return {"error":"this student is not in db"}
        
    @staticmethod
    def ListPayment():
        with SessionLocal() as db:
            data = db.query(MonthlyPayment).all()
            if data:
                return data
            return {"error": "there is not any payment in db"}