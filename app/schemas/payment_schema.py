from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class PaymentType(str, Enum):
    money = "dinheiro"
    transferencia = "transferência"


class Descriptiontype(str, Enum):
    propina = "propina"
    folha = "folha"
    boletim = "boletim"


class StatusType(str, Enum):
    pendente = "pendente"
    pago = "pago"


class PaymentCreate(BaseModel):
    student_id: int
    amount: float
    description: Descriptiontype
    number: int
    method: PaymentType


class PaymentResponse(BaseModel):
    id: int
    student_id: int
    amount: float
    description: Descriptiontype
    number: int
    method: PaymentType
    status: StatusType
    date: datetime


class PaymentMonthlyCreate(BaseModel):
    student_id: int
    month: str
    grade: int
    amount: float
    method: PaymentType


class PaymentMonthlyResponse(BaseModel):
    id: int
    student_id: int
    month: str
    grade: int
    amount: float
    method: PaymentType
    paid_at: datetime
    status: StatusType