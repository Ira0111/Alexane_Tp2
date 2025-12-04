from Member import*

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience = 0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    @property
    def _role(self):
        return self.__role

    @_role.setter
    def _role(self, value):
        self.__role = value

    @property
    def _experience(self):
        return self.__experience

    @_experience.setter
    def _experience(self, value):
        self.__experience = value

    def act(self):
        match self.__role:
            case "commandant":
                print(self.__first_name, self.__last_name, "fait des verification")
            case "technicien":
                print(self.__first_name, self.__last_name, "nettoie le vaisseau")
            case "armurier":
                print(self.__first_name, self.__last_name, "fabrique une arme")
            case "pilot":
                print(self.__first_name, self.__last_name, "s'entrainne sur un simulateur")
            case "marchand":
                print(self.__first_name, self.__last_name, "surveil son stock")
            case "entretien":
                print(self.__first_name, self.__last_name, "réparer un partie du vaisseau")
            case _:
                print(self.__first_name, self.__last_name, "rôle inconnu")   

    def gain_experience(self):
        self.__experience += 1
