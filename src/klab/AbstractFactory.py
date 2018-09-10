# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class PizzaFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print ("Prepare ", type(self).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print ("Prepare ", type(self).__name__)


class NonVegPizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def serve(self, NonVegPizza):
        pass


class ChickenPizza(NonVegPizza):
    def serve(self, NonVegPizza):
        print (type(self).__name__, " is served with Chicken on ", type(NonVegPizza).__name__)


class HamPizza(NonVegPizza):
    def serve(self, NonVegPizza):
        print (type(self).__name__, " is served with Ham on ", type(NonVegPizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()
