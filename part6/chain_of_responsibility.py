#责任链

from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):

    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):

    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是离职吧")

class DeparmentManager(Handler):

    def __init__(self):
        self.next =  GeneralManager()

    def handle_leave(self, day):

        if day <= 5:
            print("部门准假%d天" % day)
        else:
            print("权限不足")
            self.next.handle_leave(day)

de = DeparmentManager()

de.handle_leave(5)
