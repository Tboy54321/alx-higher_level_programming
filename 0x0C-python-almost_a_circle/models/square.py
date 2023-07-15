#!/usr/bin/python3
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

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
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

<<<<<<< HEAD

=======
    def to_dictionary(self):
        list_ = ["x", "y", "id",  "height"]
        list_dict = {}
        for _ in list_:
            list_dict[_] = getattr(self, _)
        return list_dict
>>>>>>> refs/remotes/origin/main
