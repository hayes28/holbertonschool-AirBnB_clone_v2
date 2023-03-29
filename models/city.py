#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    class City(BaseModel, Base):
        """ Represents a city for a MySQL database """
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place', backref="cities",
                                cascade="all, delete, delete-orphan")
else:
    class City(BaseModel):
        """
        City class
        """
        state_id= ''
        name= ''
