from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_uri = 'postgresql+psycopg2://yshfoploodevmb:5ee193514f85b2cedd439e1dcaebbfb79744384429832bddee994677d4bfe1e9@ec2-52-86-123-180.compute-1.amazonaws.com:5432/dflims91p5k23q'

engine = create_engine(db_uri)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)

    def __init__(self, id):
        self.id = id