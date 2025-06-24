from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.config import Base
from datetime import datetime

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    number = Column(Float, nullable=False)
    datetime = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="exams")