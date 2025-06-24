from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base
from datetime import datetime


class MonthlyPayment(Base):
    __tablename__ = "monthly_payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    month = Column(Integer, nullable=False)  # 1-12
    grade = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pendente")  # ou "pago", "atrasado"
    paid_at = Column(DateTime, nullable=True)
    method = Column(String, nullable=False)

    student = relationship("Student", back_populates="monthly_payments")