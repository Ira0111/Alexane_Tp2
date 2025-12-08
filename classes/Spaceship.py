from classes.Member import*
from classes.Operator import*
from classes.Mentalist import*

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
        has_pilot = False
        has_technician = False
        has_powerful_mentalist = False

        for member in self.crew:
            role = getattr(member, "role", None)
            if role == "pilot":
                has_pilot = True
            elif role == "technicien":
                has_technician = True
            if isinstance(member, Mentalist) and getattr(member, "mana", 0) >= 50:
                has_powerful_mentalist = True

        print("\n🔍 Vérification de la préparation du vaisseau", self.name)
        print("Pilote :", "Check" if has_pilot else "X")
        print("Technicien :", "Check " if has_technician else "X")
        print("Mentaliste avec mana ≥ 50 :", "Check" if has_powerful_mentalist else "X")

        return has_pilot and has_technician and has_powerful_mentalist
    
    def remove_member(self, last_name : str,):
        found = False
        for member in self.crew:
            if member.last_name == last_name:
                self.crew.remove(member)
                print(member.first_name, member.last_name, "a été retiré de l'équipage du vaisseau", self.name)
                found = True
                return
        if not found:
            print("Aucun membre avec le nom", last_name, "n'a été trouvé dans l'équipage du vaisseau", self.name)

    def display_crew(self):
        print("\n=== Équipage du vaisseau", self.name, "===")
        for member in self.crew:
            role = getattr(member, "role", "inconnu")
            if member.gender == "femme":
                print("-", member.first_name, member.last_name, "est une femme de", member.age, "ans, son role est :", role)
            elif member.gender == "homme":
                print("-", member.first_name, member.last_name, "est un homme de", member.age, "ans, son role est :", role)
