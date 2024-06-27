#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models import storage

metadata = Base.metadata,
place_amenity = Table('place_amenity', metadata,\
                    Column('place_id', String(60), ForeignKey('places.id'),\
                        primary_key=True, nullable=False),\
                    Column('amenity_id', String(60), ForeignKey('amenities.id'),\
                        primary_key=True, nullable=False)\
                    )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities_id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users_id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') is 'db':
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') is 'file':
        @property
        def amanities(self):
            """Getter attribute amenities that returns a list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id linked to the Place

            Returns:
                list: A list of Amenity instances linked to this Place
            """
            all_amenities = list(storage.all(Amenity).values())
            place_amenities = []
            place_amenities.append(a for a in all_amenities if a.id in self.amenity_ids)
            return place_amenities

        @amanities.setter
        def amanities(self, obj):
            if obj is not None and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
