#!/usr/bin/python3
"""Defines a class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that defines Amenity properties.

    Attributes:
        name (string): name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)
