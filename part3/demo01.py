#建造者模式

from abc import ABCMeta, abstractmethod

class Player(object):

    def __init__(self, eye=None, body=None, face=None):
        self.eye = eye,
        self.body = body,
        self.face = face

    def __str__(self):
        return "{},{},{}".format(self.eye, self.body, self.face)

class PlayerBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_eye(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

class GirlBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body = "窈窕的"

    def build_eye(self):
        self.player.eye = "明亮的"

    def build_face(self):
        self.player.face = "鹅蛋脸"


class MonsterBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body = "粗壮的"

    def build_eye(self):
        self.player.eye = "大"

    def build_face(self):
        self.player.face = "大大大"

class PlayerDirecter(object):

    def buildplayer(self, builder):
        builder.build_body()
        builder.build_eye()
        builder.build_face()
        return builder.player


builder = GirlBuilder()
girl = PlayerDirecter().buildplayer(builder)
print(girl)

builder = MonsterBuilder()
girl = PlayerDirecter().buildplayer(builder)
