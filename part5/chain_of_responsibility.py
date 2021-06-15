#代理模式

from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):

    def __init__(self, filename):
        self.filename = filename
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding="utf-8")
        f.write(content)
        f.close()

#虚代理
class VirtualProxy(Subject):

    def __init__(self, filename):
        self.filename = filename
        self.sub = None

    def get_content(self):
        if not self.sub:
          self.sub = RealSubject(self.filename)
        return self.sub.get_content()

    def set_content(self, content):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        self.sub.set_content(content)


#保护代理
class ProtectProxy(Subject):

    def __init__(self, filename):
        self.sub = RealSubject(filename)

    def get_content(self):
        return self.sub.get_content()

    def set_content(self, content):
        raise PermissionError("权限不足")

virtualProxy = VirtualProxy("text.txt")
virtualProxy.set_content("22222")
protectProxy = ProtectProxy("text.txt")
print(protectProxy.get_content())
protectProxy.set_content("322222")

