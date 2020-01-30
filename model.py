from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Question (Base):
   __tablename__ = 'question'
   id = Column(Integer, primary_key=True)
   content = Column(String)
   writer = Column(String)

class Answer (Base):
	__tablename__ = 'answer'
	id = Column(Integer, primary_key=True)
	content = Column(String)