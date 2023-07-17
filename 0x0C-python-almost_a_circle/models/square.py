#!/usr/bin/python3
"""Creating my Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Created a Rectangle Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Define the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size property"""
        self.width = value
        self.height = value

    def __str__(self):
        """Redefine the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Define the update method"""
        list_ = ["id", "size", "x", "y"]
        if args is not None and bool(args) is True:
            x = 0
            for _ in list_:
                try:
                    """args[x] = list_[x]"""
                    setattr(self, _, args[x])

                except IndexError:
                    pass
                x += 1
        else:
            for _ in list_:
                try:
                    setattr(self, _, kwargs[_])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Define the to_dictionary method"""
        list_ = ["x", "y", "id",  "height"]
        list_dict = {}
        for _ in list_:
            list_dict[_] = getattr(self, _)
        return list_dict
