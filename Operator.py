from Member import*

class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role, experience):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience
    
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
                print(self.__first_name, self.__last_name, "commande son stock")
            case _:
                print(self.__first_name, self.__last_name, "rôle inconnu")        
        