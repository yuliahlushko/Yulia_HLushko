class Train:
    def __init__(self, name):
        self.name = name
        self.carriages = []

    def add_carriage(self, carriage):
        if isinstance(carriage, Carriage):
            self.carriages.append(carriage)

    def __str__(self):
        return f"{self.name} Train with {len(self.carriages)} carriages."

class Carriage:
    def __init__(self, number, places):
        self.number = number
        self.capacity = places
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger} added to Carriage {self.number}")

    def __str__(self):
        return f"Carriage {self.number} (Total places: {self.capacity}, Occupied: {len(self.passengers)})"


class Passenger:
    def __init__(self, name, destination, place):
        self.name = name
        self.destination = destination
        self.place = place

    def __str__(self):
        return self.name

train = Train("Express")
passenger1 = Passenger("Yulia", 'Kyiv', 7)
passenger2 = Passenger("Maks", 'Nyzhyn', 8)
passenger3 = Passenger("Slava", 'Gatne', 9)
carriage1 = Carriage(1, 50)
carriage2 = Carriage(2, 40)
train.add_carriage(carriage1)
train.add_carriage(carriage2)
carriage1.add_passenger(passenger1)
carriage1.add_passenger(passenger2)
carriage2.add_passenger(passenger3)

print(train)
for carriage in train.carriages:
    print(carriage)

for passenger in carriage1.passengers:
    print(f'Passenger: {passenger.name}, place: {passenger.place}, destination: {passenger.destination}')

for passenger in carriage2.passengers:
    print(f'Passenger: {passenger.name}, place: {passenger.place}, destination: {passenger.destination}')