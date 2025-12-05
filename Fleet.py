from Member import*
from Operator import*
from Spaceship import*


class Spaceship:
    def __init__(self, name):
        self.__name = name
        self.__spaceship = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def spaceship(self):
        return self.__spaceship

    @spaceship.setter
    def spaceship(self, value):
        self.__spaceship = value

    def append_spaceship(self, spaceship: Spaceship):
        if len(self.crew) >= 15:
            print("La Flotte est complette : imposible d'ajouter", spaceship.name)
        else:
            self.spaceship.append(spaceship)
            print(spaceship.name, "a été ajouter dans la flotte", self.name)
