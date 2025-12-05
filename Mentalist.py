from Member import*
from Operator import*

class Mentalist(Member):
    def __init__(self, first_name, last_name, gender, age, mana = 100):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana 

    @property
    def _mana(self):
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = max(0, min(100, value))

    def act(self, operator):
        if self.__mana <20:
            print(self.__first_name, self.__last_name, "n'as pas assez de mana pour agir")
        else:
            self.__mana -= 20
            print(self.__first_name, self.__last_name, "influence", operator.__first_name, operator.__last_name, "pour agir :")
            operator.act()
        
    def recharge_mana(self):
        self.__mana = min(100, self.__mana + 50)
        print(self._first_name, self._last_name, "recharge son mana à", self.__mana)

