#单例
class Singleton(type):

    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):

        if not self._instance:
            self._instance = super.__call__(*args, **kwargs)

        return self._instance

class Car(metaclass=Singleton):

    def __init__(self):
        pass

car1 = Car()
car2 = Car()

print(car1 is car2)
