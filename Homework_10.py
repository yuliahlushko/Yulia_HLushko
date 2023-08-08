from abc import ABC, abstractmethod

class Cars:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @abstractmethod
    def takePartInRace(self):
        pass


class Racer(Cars):
    def __init__(self, brand, color, number):
        super().__init__(brand, color)
        self.number = number

    def registration(self):
        print("You are successfully registered in the race!")


class Characteristics(Racer):
    def __init__(self, brand, color, number, maxSpeed, engine):
        super().__init__(brand, color, number)
        self.maxSpeed = maxSpeed
        self.engine = engine

    def info(self):
        print(f'Your parameters are: {self.brand}, color is {self.color}. Your number is {self.number}. Max speed is {self.maxSpeed} km')

    def chanceToWin(self):
        if self.maxSpeed and self.engine>1.5:
            print('You have a great chance to win!')
        else:
            print('Your characteristics enough to win!')

McQueen = Racer("Porshe", "Red", 95)
McQueen.registration()
McQueen = Characteristics('Porshe', 'Red', 95, 500, 2)
McQueen.info()
McQueen.chanceToWin()