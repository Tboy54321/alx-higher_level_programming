#!/usr/bin/python3

import json
from . import rectangle

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file = "{}.json".format(cls.__name__)
        list_ = []
        if list_objs is None:
            return []
        else:
            for _ in list_objs:
                dict = _.to_dictionary()
                list_.append(dict)
            json_file = Base.to_json_string(list_)

        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_file)

    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base and returns a instance with all
           attributes already set
        Args:
           dictionary: Dictionary with all attributes of the object
        Return:
           A instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances
           - the type of these instances depends on cls
        """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list