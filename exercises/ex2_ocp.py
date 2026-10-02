import random
from engine.track import Track


class Vehicle:

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class Car(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class Truck(Vehicle):
    symbol = "\U0001F69A"

    def move(self) -> None:
        self.position += 2


class Motorcycle(Vehicle):
    symbol = "\U0001F3CD"

    def move(self) -> None:
        self.position += random.randint(2, 9)


class Bicycle(Vehicle):
    symbol = "\U0001F6B2"

    def __init__(self, name: str):
        super().__init__(name)
        self.energy = 8

    def move(self) -> None:
        self.position += self.energy
        self.energy = max(self.energy - 1, 1)



def main():
    vehicles = [
        Car("Red Car"),
        Truck("Big Rig"),
        Motorcycle("Ghost Rider"),
        Bicycle("Pedal Pete"),
    ]
    Track(length=35).run(vehicles)


if __name__ == "__main__":
    main()
