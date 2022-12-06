import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    user_vk_id = sq.Column(sq.Integer, primary_key=True)


class Recommendations(Base):
    __tablename__ = 'recommendations'

    recommendation_id = sq.Column(sq.Integer, primary_key=True)
    user_vk_id = sq.Column(sq.Integer, sq.ForeignKey('users.user_vk_id'))
    partner_vk_id = sq.Column(sq.Integer)

    user = relationship(Users, backref='recommendation')

def create_tables(engine):
    Base.metadata.create_all(engine)
