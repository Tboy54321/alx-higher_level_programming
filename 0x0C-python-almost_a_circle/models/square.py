# !/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args):
        list_ = ["id", "size", "x", "y"]
        if args is not None:
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

        
