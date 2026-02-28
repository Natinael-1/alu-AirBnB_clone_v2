#!/usr/bin/python3
"""State Module for HBNB project"""

import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan"
        )
    else:

        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equals to the current State.id."""
            return [
                city
                for city in models.storage.all(City).values()
                if city.state_id == self.id
            ]
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models import storage
            from models.city import City
            
            city_list = []
            # Get all City objects from storage
            for city in storage.all(City).values():
                # Check if the city's state_id matches this state's id
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
