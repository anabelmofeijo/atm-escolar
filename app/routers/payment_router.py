from fastapi import APIRouter
from app.schemas.payment_schema import PaymentCreate, PaymentMonthlyCreate
from app.services.payment_service import PaymentService, MonthlyPaymentService

router = APIRouter()

@router.get("/")
async def run():
    return {"message": "payment is running"}

@router.post("/create/")
async def create_payment(data: PaymentCreate):
    service = PaymentService
    response = service.CreatePayment(new_data=data.dict())
    return response

@router.get("/list-payments/")
async def list_payments():
    service = PaymentService()
    response = service.ListPayment()
    return response

@router.get("/list-payment-by-student/{student_id}")
async def list_payment_by_student(student_id: int):
    service = PaymentService()
    response = service.ListPaymentByStudent(student_id)
    return response

@router.delete("/delete/{id}")
async def delete(id: int):
    service = PaymentService()
    response = service.DeletePayment(id)
    return response


# Monthly Payment

@router.post("/monthly/create/")
async def create_payment(data: PaymentMonthlyCreate):
    service = MonthlyPaymentService
    response = service.CreatePayment(new_data=data.dict())
    return response

@router.get("/monthly/list-payments/")
async def list_payments():
    service = MonthlyPaymentService()
    response = service.ListPayment()
    return response

@router.get("/monthly/list-payment-by-student/{student_id}")
async def list_payment_by_student(student_id: int):
    service = MonthlyPaymentService()
    response = service.ListPaymentByStudent(student_id)
    return response

@router.delete("/monthly/delete/{id}")
async def delete(id: int):
    service = PaymentService()
    response = service.DeletePayment(id)
    return response