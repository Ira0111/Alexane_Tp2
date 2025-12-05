from Member import*

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience = 0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

    def act(self):
        match self.role:
            case "commandant":
                print(self.first_name, self.last_name, "fait des verification")
            case "technicien":
                print(self.first_name, self.last_name, "nettoie le vaisseau")
            case "armurier":
                print(self.first_name, self.last_name, "fabrique une arme")
            case "pilot":
                print(self.first_name, self.last_name, "s'entrainne sur un simulateur")
            case "marchand":
                print(self.first_name, self.last_name, "surveil son stock")
            case "entretien":
                print(self.first_name, self.last_name, "réparer un partie du vaisseau")
            case _:
                print(self.first_name, self.last_name, "rôle inconnu")   

    def gain_experience(self):
        self.experience += 1
