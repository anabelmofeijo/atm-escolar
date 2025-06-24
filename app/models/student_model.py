from sqlalchemy import Column, Integer, String
from app.core.config import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    student_number = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)