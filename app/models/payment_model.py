from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base
from datetime import datetime


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False) # propina, boletim, folha de prova
    number = Column(Integer, nullable=False) # numero de folhas
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pendente")  # ou "pago", "atrasado"
    method = Column(String, nullable=False)

    student = relationship("Student", back_populates="payments")