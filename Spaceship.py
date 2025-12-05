from Member import*
from Operator import*


class Spaceship:
    def __init__(self, name, shipType, condition="opérationnel"):
        self.__name = name
        self.__shipType = shipType
        self.__crew = []
        self.__condition = condition 

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def shipType(self):
        return self.__shipType

    @shipType.setter
    def shipType(self, value):
        self.__shipType = value

    @property
    def crew(self):
        return self.__crew

    @crew.setter
    def crew(self, value):
        self.__crew = value


    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        self.__condition = value

    def append_member(self, member: Member):
        if len(self.crew) >= 10:
            print("L'équipage est complet : imposible d'ajouter", member.first_name, member.last_name)
        else:
            self.crew.append(member)
            print(member.first_name, member.last_name, "a été ajouter à l'équipage du vaisseau", self.name)

    def check_preparation(self):
        has_technician = False
        has_pilot = False
        if len(self.crew) >= 2:
            for member in self.crew:
                if isinstance(member, Operator):
                    if member.role == "pilot":
                        has_pilot = True
                    elif member.role == "technicien":
                        has_technician = True
        return has_technician and has_pilot
    
    def display_crew(self):
        print("👥 Équipage du vaisseau", self.name)
        for member in self.crew:
            role = getattr(member, "role", "inconnu")
            print("-", member.first_name, member.last_name, "(", role, ")")
