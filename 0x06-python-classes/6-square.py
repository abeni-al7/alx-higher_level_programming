#!/usr/bin/python3
"""
Defines a class with attributes.
"""
class Square:
    """
     A simple square class with attributes.
     
     Attributes:
        size (int): the length of the side of the square
        position (tuple): space position
 
    Methods:
        area: area of the square
        my_print: prints the square object
    """
    def __init__(self, size=0, position=(0,0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple and len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value
        if type(self.__position) is not tuple and len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
        lines = self.__position[1]
        for i in range(self.__size + lines):
            spaces = self.__position[0]
            if lines != 0:
                print()
                lines -= 1
                continue
            for j in range(self.__size + spaces):
                if spaces != 0:
                    print(" ", end="")
                    spaces -= 1
                    continue
                print("#", end="")
            print()
