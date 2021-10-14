from sqlalchemy import Column, String
from .entity import Entity, Base

class Player(Entity, Base):
    __tablename__ = 'player'

    codename = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, id, codename, first_name="", last_name=""):
        super().__init__(id)
        self.codename = codename
        self.first_name = first_name
        self.last_name = last_name