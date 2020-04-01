#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel
from models.base_model import Base


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
    cities = relationship("City", backref="state", cascade="all, delete")


    @property
    def cities(self):
        """
        Returns the list of City instances with state_id equals to the current
        State.id as private
        """
        c_list = []
        for city_id, value in models.storage.all(City).items():
            if city_id.state_id == self.id:
                return c_list.append(value)
