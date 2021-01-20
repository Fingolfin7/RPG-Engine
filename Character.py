import random
import math


class Character:
    def __init__(self, name, health, strength, block):
        self.name = name
        self.health = health
        self.strength = strength
        self.block = block

    def __str__(self):
        return "Name: {}, health: {}, strength: {}, block: {}.".format(self.name, self.health,
                                                                       self.strength, self.block)

    @property
    def name(self):
        return self.__name

    @property  # getter
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    @property
    def block(self):
        return self.__block

    @name.setter
    def name(self, value):
        self.__name = value

    @health.setter
    def health(self, value):
        self.__health = value

    @strength.setter
    def strength(self, value):
        self.__strength = value

    @block.setter
    def block(self, value):
        self.__block = value

    def attack(self):
        return math.floor(random.random() * self.__strength)  # random.random() gets a random number between 0 and 1

    def getBlock(self):
        return math.floor(random.random() * self.__block)