#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


link_table = Table("place_amenity", Base.metadata,
                   Column("place_id", ForeignKey("places.id"), nullable=False),
                   Column("amenity_id", ForeignKey("amenities.id"), nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest =  Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    # took out back_populates, see if it is needed
    amenities = relationship("Amenity", secondary=link_table, viewonly=False)

    @property
    def reviews(self):
        """
        Returns the list of Review instances with place_id equals to the current
        Place.id as private
        """
        c_list = []
        for key, value in models.storage.all(Review).items():
            if key.place_id == self.id:
                return c_list.append(value)

    @property
    # Getter
    # once data from setter gets to the getter, (which is the amenity_id)
    def amenities(self):
        """
        Returns list of Amenity instances based on the attribute amenity_ids
        that contains all Amenity.id linked to the Place
        """
        a_list = []
        for key, value in models.storage.all(Amenity).items():
            if key.amenity_ids == self.id:
                return a_list.append(value)

    @amenities.setter
    def amenities(self, value):
        """
        Handles append method for adding an Amenity.id to the attribute
        amenity_ids. This method should accept only Amenity object,
        otherwise, do nothing
        """
        if type(value) is Amenity:
            self.amenity_ids.append(value.id)
