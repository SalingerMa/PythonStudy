# -*- coding: utf-8 -*-
class Employees():

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"<Employee: name={self.name}, salary={self.salary}>"

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(f"{self.name} dose stuff")


class Chef(Employees):
    def __init__(self, name):
        Employees.__init__(self, name, 50000)

    def work(self):
        print(f'{self.name} makes food')


class Server(Employees):
    def __init__(self, name):
        Employees.__init__(self, name, 40000)

    def work(self):
        print(f'{self.name} servers to customer')

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(f'{self.name} makes pizza')

if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob.salary)

    for k in Employees, Chef, Server, PizzaRobot:
        obj = k(k.__class__)
        obj.work()