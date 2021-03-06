# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.exam import Exam

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Exam).all()


    # create and persist dummy exam
python_exam = Exam("Test", "Test your knowledge about SQLAlchemy.", "script")
session.add(python_exam)
session.commit()
session.close()

    # reload exams
exams = session.query(Exam).all()

# show existing exams
print('### Exams:')
