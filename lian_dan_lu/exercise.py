# coding: utf-8

# class Goods(object):
#     def __init__(self, price, discount):
#         self.price = price
#         self.discount = discount
#
#     def getPrice(self):
#         return self.price * self.discount
#
#     def setPrice(self, value):
#         self.price = value

# goods = Goods(30, 0.8)
# print('商品折扣后售价：', goods.getPrice())
# goods.setPrice(40)
# print("商品价格变为：", goods.getPrice())

# class GoodsPro(object):
#     def __init__(self, price, discount):
#         self.price = price
#         self.discount = discount
#
#     @property
#     def priceInfo(self):
#         return self.price * self.discount
#
#     @priceInfo.setter
#     def priceInfo(self, value):
#         self.price = value
#
#     @priceInfo.deleter
#     def priceInfo(self):
#         del self.price
#
# goodspro = GoodsPro(30, 0.8)
# print('商品折扣后售价：', goodspro.priceInfo)
# # 设置商品价格
# goodspro.price = 40
# # 获取折扣后商品价格
# print("商品价格变为：", goodspro.priceInfo)

# Bob
# class Money:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
# money = Money(27, 12)
# message = "I have {:d} dollars and {:d} cents."
# print(message.format(money.dollars, money.cents))
# "I have 27 dollars and 12 cents."
# money.dollars += 2
# money.cents += 20
# print(message.format(money.dollars, money.cents))

# Alice
# class Money:
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
# Alice最终版本
class Money(object):
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # dollars使用property装饰器的输入、输出
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # cents使用property装饰器的输入、输出
    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents

s = Money(1,2)
print(s.dollars)
print(s.cents)
# cents改变之后执行cents.setter
s.cents += 112
print(s.dollars)
print(s.cents)


# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.score = 60.6
# print(s.score)
# s.score = 9999