from Member import*
from Operator import*


class Spaceship:
    def __init__(self, name, shipType, condition="opérationnel"):
        self.__name = name
        self.__shipType = shipType
        self.__crew = []
        self.__condition = condition

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _shipType(self):
        return self.__shipType

    @_shipType.setter
    def _shipType(self, value):
        self.__shipType = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        if isinstance(value, list):
            self.__crew = value
        else:
            print("Erreur : crew doit être une liste")

    @property
    def _condition(self):
        return self.__condition

    @_condition.setter
    def _condition(self, value):
        self.__condition = value

    def append_member(self, member: Member):
        if self.__crew >= 10:
            print("L'Equipage est complet : imposible d'ajouter", member.__first_name, member.__last_name)
        else:
            self.__crew.append(member)
            print(member.__first_name, member.__last_name, "a été ajouter à l'equipage du vaisseau", self.__name)

    def check_preparation(self):
        has_technician = False
        has_pilot = False
        if len(self.__crew) >= 2:
            for member in self.__crew:
                if isinstance(member, Operator):
                    if member._role == "pilot":
                        has_pilot = True
                    elif member._role == "technicien":
                        has_technician = True
        return has_technician and has_pilot
