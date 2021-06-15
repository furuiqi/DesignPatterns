#桥模式

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def _name(self):
        pass

class Color(metaclass=ABCMeta):

    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):

    def draw(self):
        self.color.paint(self)

    def _name(self):
        return "长方形"


class Circle(Shape):

    def draw(self):
        self.color.paint(self)

    def _name(self):
        return "圆形"


class Red(Color):

    def paint(self, shape):
        print("红色的{}".format(shape._name()))


class Green(Color):

    def paint(self, shape):
        print("绿色的{}".format(shape._name()))


shape = Rectangle(Red())
shape.draw()

shape = Rectangle(Green())
shape.draw()
