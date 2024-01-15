#!/usr/bin/python3
"""The module for the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """An initializer method"""
        super().__init__(id)
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle object"""
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for space in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.__width
        my_dict["height"] = self.__height
        my_dict["x"] = self.__x
        my_dict["y"] = self.__y
        return my_dict

    def __str__(self):
        """Prints the Rectangle"""
        return '[Rectangle] ({}) {}/{} -
                {}/{}'.format(self.id, self.__x, self.__y, 
                               self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle"""
        if len(args) > 0 and isinstance(args[0], int):
            self.id = args[0] 
        if len(args) > 1 and isinstance(args[1], int):
            self.__width = args[1]
        if len(args) > 2 and isinstance(args[2], int):
            self.__height = args[2]
        if len(args) > 3 and isinstance(args[3], int):
            self.__x = args[3]
        if len(args) > 4 and isinstance(args[4], int):
            self.__y = args[4]
        if args is None or len(args) == 0:
            if "id" in kwargs and isinstance(kwargs["id"], int):
                self.id = kwargs["id"]
            if "width" in kwargs and isinstance(kwargs["width"], int):
                self.__width = kwargs["width"]
            if "height" in kwargs and isinstance(kwargs["height"], int):
                self.__height = kwargs["height"]
            if "x" in kwargs and isinstance(kwargs["x"], int):
                self.__x = kwargs["x"]
            if "y" in kwargs and isinstance(kwargs["y"], int):
                self.__y = kwargs["y"]
