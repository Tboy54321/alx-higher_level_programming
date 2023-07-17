#!/usr/bin/python3

import json
from . import rectangle
import turtle
import csv

class Base:
    """Defines Base Class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initailze the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To json string"""
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
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
        """From json string method"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create class method"""
        if cls.__name__ == "Rectangle":
            sample_file = cls(1, 1)
        elif cls.__name__ == "Square":
            sample_file = cls(1)
        sample_file.update(**dictionary)
        return sample_file

    @classmethod
    def load_from_file(cls):
        """Load from file method"""
        file = "{}.json".format(cls.__name__)
        list_ = []

        try:
            with open(file, 'r') as f:
                json_string = f.read()
                dict_list = cls.from_json_string(json_string)
                for item in dict_list:
                    instance = cls.create(**item)
                    list_.append(instance)
        except FileNotFoundError:
            return list_

        return list_

    # @classmethod
    # def save_to_file_csv(cls, list_objs):
    #     file = "{}.csv".format(cls.__name__)
    #     list_ = []
    #     if list_objs is not None:
    #         for _ in list_objs:
    #             dictionary = _.to_dictionary()
    #             list_.append(dictionary)
    #     rectangle_header = ['id', 'width', 'height', 'x', 'y']
    #     square_header = ['id', 'size', 'x', 'y']
    #     with open(file, mode='w') as x:
    #         if list_objs is None:
    #             x.write("[]")
    #         else:
    #             if cls.__name__ == 'Rectangle':
    #                 result = csv.DictWriter(x, fieldnames=rectangle_header)
    #             elif cls.__name__ == 'Square':
    #                 result = csv.DictWriter(x, fieldnames=square_header)
    #             result.writeheader()
    #             result.writerows(list_)

    # @classmethod
    # def load_from_file_csv(cls):
    #     filename = "{}.csv".format(cls.__name__)
    #     instance_list = []
    #     try:
    #         with open(filename) as f:
    #             result = csv.DictReader(f)
    #             for row in result:
    #                 row = dict(row)
    #                 for key in row:
    #                     row[key] = int(row[key])
    #                 instance = cls.create(**row)
    #                 instance_list.append(instance)
    #     except FileNotFoundError:
    #         return instance_list
    #     return instance_list

    # @staticmethod
    # def draw(list_rectangles, list_squares):
    #     # Open screen and set the turtle in the center
    #     s = turtle.getscreen()
    #     t = turtle.Turtle()
    #
    #     # Add a title to my screen
    #     turtle.title("My first draw with python and tutle module")
    #
    #     # Customize turtle and screen background
    #     t.shape("turtle")
    #     turtle.bgcolor("black")
    #
    #     # Customize pen for rectangle
    #     t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
    #     # Extract the data from the instance rectangle list
    #     for instance in list_rectangles:
    #         # Customize pen for rectangle
    #         t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
    #         data = instance.to_dictionary()
    #         # Set the position acording the rectangle object
    #         t.home()
    #         t.setpos(data['x'], data['y'])
    #         # Draw process
    #         t.pd()
    #         for i in range(2):
    #             t.forward(data['width'])
    #             t.left(90)
    #             t.forward(data['height'])
    #             t.left(90)
    #         t.pu()
    #
    #     # Customize pen for square
    #     t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)
    #     # Extract the data from the instance square list
    #     for instance in list_squares:
    #         data = instance.to_dictionary()
    #         # Set the position acording the square object
    #         t.home()
    #         t.setpos(data['x'], data['y'])
    #         # Draw process
    #         t.pd()
    #         for i in range(4):
    #             t.forward(data['size'])
    #             t.left(90)
    #         t.pu()
    #
    #     # Keeps window open
    #     turtle.getscreen()._root.mainloop()