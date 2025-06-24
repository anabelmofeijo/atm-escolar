from fastapi import APIRouter
from app.schemas.payment_schema import PaymentCreate
from app.services.payment_service import PaymentService

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
