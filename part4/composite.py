# 组合模式

from abc import ABCMeta, abstractmethod

class Graphic(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass

class Point(Graphic):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点({},{})".format(self.x, self.y)

    def draw(self):
        print(self)

class Line(Graphic):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段([{},{}])".format(self.p1, self.p2)

    def draw(self):
        print(self)

class Picture(Graphic):

    def __init__(self, iterable):
        self.children = []
        for _ in iterable:
            self._add(_)

    def _add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        for _ in self.children:
            _.draw()

p1 = Point(1, 2)
p2 = Point(3, 4)
l1 = Line(p1, p2)
l2 = Line(p2, p1)

pic1 = Picture([p1, p2])
#pic1.draw()

pic2 = Picture([l1, p2])
#pic2.draw()

pic3 = Picture([pic1, pic2])
pic3.draw()
