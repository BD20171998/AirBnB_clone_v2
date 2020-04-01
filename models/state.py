#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        state_id: The state id
        name: input name
    """

    """This init method allows the class to access BaseModel's attributes"""
    def __init__(self):
        BaseModel.__init__(self)

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete",)

    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals to the current
        State.id as private
        """
        #session.query(State, City).filter(City.state_id == State.id).all()

        results = self.storage.all()
        print(results)
        return self.__results
