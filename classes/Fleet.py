from classes.Member import*
from classes.Operator import*
from classes.Spaceship import*

class Fleet:
    def __init__(self, name):
        self.__name = name
        self.__spaceships = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def spaceships(self):
        return self.__spaceships

    @spaceships.setter
    def spaceships(self, value):
        self.__spaceships = value

    def append_spaceship(self, spaceship: Spaceship):
        if len(self.spaceships) >= 15:
            print("La Flotte est complette : imposible d'ajouter", spaceship.name)
        else:
            self.spaceships.append(spaceship)

    def statistics(self):
        total_members = 0
        role_count = {}
        total_experience = 0
        operator_count = 0
        for ship in self.spaceships:
            for member in ship.crew:
                total_members += 1
                role = None
                if isinstance(member, Operator):
                    operator_count += 1
                    total_experience += member.experience
                    role = member.role
                else:
                    role = getattr(member, "role", "inconnu")

                role_count[role] = role_count.get(role, 0) + 1

        print("===Statistiques de la flotte===", self.name)
        print("Nombre total de membres :", total_members)
        print("Répartition des rôles :")
        for role, count in role_count.items():
            print("-", role, ":", count)

        if operator_count > 0:
            moyenne = round(total_experience / operator_count, 2)
            print("Niveau moyen d'expérience des opérateurs :", moyenne)
        else:
            print("Aucun opérateur dans la flotte.")
