import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model import create_tables

with open("postgresql_password.txt", "r") as file_object:
    db_password = file_object.read().strip()

DSN = f"postgresql+psycopg2://postgres:{db_password}@localhost:5432/vkinder"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
