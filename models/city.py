#!/usr/bin/python3
"""Defines a class City that inherits from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines City properties.

    Attributes:
        name (string): name of city.
        state_id (string): id of state.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of City.
        """
        super().__init__(*args, **kwargs)
