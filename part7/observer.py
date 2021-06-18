#观察者模式

from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, notice):
        pass


class Notice:

    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notity(self):
        for obs in self.observers:
            obs.update(self)

class StaffNotice(Notice):

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notity()

class Staff(Observer):

    def __init__(self, name):
        self.company_info = None
        self.name = name

    def update(self, notice):
        self.company_info = notice.company_info

    def data(self):
        print(self.name, self.company_info)

staff = StaffNotice("初始化")
s1 = Staff("老王")
s2 = Staff("老张")
s1.data()
s2.data()
staff.attach(s1)
staff.attach(s2)
s1.data()
s2.data()
staff.company_info = "起飞"
s1.data()
s2.data()
