import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Homework(Base):
    __tablename__ = 'homework'

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey('course.course_id'), nullable=False)

    course = relationship(Course, backref='homeworks')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# class Users(Base):
#     __tablename__ = 'users'
#
#     user_vk_id = sq.Column(sq.Integer, primary_key=True)
#
#     # recommendation = relationship('Recommendations', back_populates='user')
#
# class Recommendations(Base):
#     __tablename__ = 'recommendations'
#
#     recommendation_id = sq.Column(sq.Integer, primary_key=True)
#     user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('users.user_vk_id'))
#     partner_vk_id = sq.Column(sq.Integer)
#
#     # user = relationship(Users, back_populates='recommendation')
#     user = relationship(Users, backref='recommendation')
