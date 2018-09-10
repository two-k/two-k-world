# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print ("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print ("Meow Meow!!")


# forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


# client code
if __name__ == "__main__":
    ff = ForestFactory()
    # sel = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound("Cat")  # ff.make_sound(sel)