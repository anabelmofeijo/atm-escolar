from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.config import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    student_number = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    payments = relationship("Payment", back_populates="student", cascade="all, delete-orphan")
    monthly_payments = relationship("MonthlyPayment", back_populates="student", cascade="all, delete-orphan")
    exams = relationship("Exam", back_populates="student", cascade="all, delete-orphan")