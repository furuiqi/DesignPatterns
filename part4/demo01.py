from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):

    def pay(self, money):
        print("支付宝支付{}元".format(money))



class WechatPay(Payment):

    def pay(self, money):
        print("微信支付{}元".format(money))


class AppPay(object):

    def cost(self, money):
        print("ios支付{}元".format(money))

# 类适配
class NewAppPay(Payment, AppPay):

    def pay(self, money):
        self.cost(money)

# 组合适配
class PaymentAdapter(Payment):

    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(AppPay())
p.pay(111)

p = NewAppPay()
p.pay(222)
