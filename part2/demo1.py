#抽象工厂
class BMW(object):

    def __repr__(self):
        return "This is BMW"

class Benz(object):

    def __repr__(self):
        return "This is Benz"

class BMW_SUV(object):

    def __repr__(self):
        return "This is BMW_SUV"

class Benz_SUV(object):

    def __repr__(self):
        return "This is Benz_SUV"

class AbsFactory(object):

    def produce_car(self):
        pass

    def produce_suv(self):
        pass

class BMWFactory(AbsFactory):

    def produce_car(self):
        return BMW()

    def produce_suv(self):
        return BMW_SUV()

class BenzFactory(AbsFactory):

    def produce_car(self):
        return Benz()

    def produce_suv(self):
        return Benz_SUV()


def main():
    """
    我们可以通过特定的工厂来获得特定的产品
    """
    car1 = BenzFactory().produce_car()
    suv1 = BenzFactory().produce_suv()
    car2 = BMWFactory().produce_car()
    suv2 = BMWFactory().produce_suv()
    print(f'car1: {car1}')
    print(f'car2: {car2}')
    print(f'suv1: {suv1}')
    print(f'suv2: {suv2}')


if __name__ == "__main__":
    main()
