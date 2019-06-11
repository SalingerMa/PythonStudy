# -*- coding: utf-8 -*-
from employees import PizzaRobot, Server

class Customer(object):
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f'{self.name} orders from {server}')

    def pay(self, server):
        print(f'{self.name} pays for item to {server}')


class Oven(object):
    def bake(self):
        print('oven bakes')


class PizzaShop(object):
    def __init__(self):
        self.server = Server("Patter")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scren = PizzaShop()
    scren.order('Homer')
    print('...')
    scren.order('Shaggy')