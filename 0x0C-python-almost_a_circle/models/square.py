#!/usr/bin/python3
"""The module for the square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """An initializer method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for side length"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for side length"""
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('height must be > 0')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the Square"""
        if len(args) > 0 and isinstance(args[0], int):
            self.id = args[0] 
        if len(args) > 1 and isinstance(args[1], int):
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2 and isinstance(args[2], int):
            self.x = args[2]
        if len(args) > 3 and isinstance(args[3], int):
            self.y = args[3]
        if args is None or len(args) == 0:
            if "id" in kwargs and isinstance(kwargs["id"], int):
                self.id = kwargs["id"]
            if "size" in kwargs and isinstance(kwargs["size"], int):
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs and isinstance(kwargs["x"], int):
                self.x = kwargs["x"]
            if "y" in kwargs and isinstance(kwargs["y"], int):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of Square"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.width
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict

    def __str__(self):
        """Prints the Square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)
