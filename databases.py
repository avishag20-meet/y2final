from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_question(content, writer):
    question_object = Question(
    	content = content, 
    	writer = writer
)
    session.add(question_object)
    session.commit()

def delete_question(their_id):
	session.query(Question
		).filter_by(
		id=their_id).delete()
	session.commit()

def query_all():
	questions = session.query(
		Question).all()
	return questions

def query_by_id(their_id):
	questions = session.query(
       Question).filter_by(
       id=their_id).first()
	return question
