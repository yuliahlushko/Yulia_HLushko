from abc import ABC, abstractmethod


class Exibit(ABC):

    def __init__(self, kind:str, cost:int, century:int, name:str, author:str):
        self.kind = kind
        self._cost = cost
        self.century = century
        self.name = name
        self.author = author


    def __authenticity(self):
        return 'Fake'

    def secret(self):
        self.__authenticity()
        print('It is fake exibit')

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost


class Painting(Exibit):
    def __init__(self, kind, cost, century, name, author):
        super().__init__(kind, cost, century, name, author)

    def info(self):
        print(self.name, self.author)
class Sculpture(Exibit):
    def __init__(self, kind, cost, century, name, author):
        super().__init__(kind, cost, century, name, author)

    def info(self):
        print(self.name, self.author)


Sunflowers = Painting('picture', 6000, 17, 'Sunflowers', 'Vincent van Gogh')
Sunflowers.info()
David = Sculpture('sculpture', 12000, 14, 'David', 'Michelangelo')
David.info()
Sunflowers.secret()
David.secret()
print(Sunflowers.cost)
Sunflowers.cost = 6500
print(Sunflowers.cost)
