#!/usr/bin/python3
"""The module for the base class"""
import json


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """An initializer method"""
        if id != None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of an object"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError('list_dictionaries must be a list of dictionaries')
        for item in list_dictionaries:
            if type(item) != dict:
                raise TypeError('list_dictionaries must be a list of dictionaries')
        json_string = json.dumps(list_dictionaries)
        return json_string
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Save an object in a file"""
        name = cls.__name__ + ".json"
        json_dict = []
        for item in list_objs:
            my_dict = cls.to_dictionary(item)
            json_dict.append(my_dict)
        json_string = cls.to_json_string(json_dict)
        with open(name, "w", encoding="utf-8") as my_file:
            if list_objs == None:
                my_file.write("[]")
            else:
                my_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON representation to an object"""
        if json_string == None or json_string == "":
            return []
        my_list = json.loads(json_string)
        return my_list
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        dummy = cls(2, 2)
        cls.update(dummy, **dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of objects from a file"""
        name = cls.__name__ + ".json"
        my_list = []
        obj_list = []
        try:
            with open(name, "r") as my_file:
                json_string = my_file.read()
                my_list = cls.from_json_string(json_string)
            for dictionary in my_list:
                obj_list.append(cls.create(**dictionary))
            return obj_list
        except FileNotFoundError:
            return []
