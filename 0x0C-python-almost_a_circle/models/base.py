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
        if cls.__name__ == "Rectangle":
            sample_file = cls(1, 1)
        elif cls.__name__ == "Square":
            sample_file = cls(1)
        sample_file.update(**dictionary)
        return sample_file

    @classmethod
    def load_from_file(cls):
        file = "{}.json".format(cls.__name__)
        list_ = []
        try:
            with open(file, 'r') as f:
                json_string = f.read()
                dict_list = cls.from_json_string(json_string)
                for _ in dict_list:
                    instance = cls.create(**_)
                    list_.append(instance)
        except FileNotFoundError:
            return list_
        return list_