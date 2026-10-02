from abc import ABC, abstractmethod

from engine.track import Track

class Movable(ABC):
    @abstractmethod
    def move(self) -> None: ...

class Refuelable(ABC):
    @abstractmethod
    def refuel(self) -> None: ...

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None: ...

class Pedalable(ABC):
    @abstractmethod
    def pedal_harder(self) -> None: ...

class GasCar(Movable, Refuelable):
    symbol = "\U0001F697"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 4

    def refuel(self):
        print(f"{self.name} refuels at the gas station.")


class Bicycle(Movable, Pedalable):
    symbol = "\U0001F6B2"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3

    def pedal_harder(self):
        self.position += 1
        print(f"{self.name}'s rider pedals harder!")

class Drone(Movable, Flyable):
    symbol = "\U0001F6F8"
    
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 5

    def fly(self):
        print(f"{self.name} is flying OMG!!!")

def main():
    vehicles = [GasCar("Racer"), Bicycle("Pedal Pete"), Drone("Sky Scout")]
    Track(length=30).run(vehicles)


if __name__ == "__main__":
    main()
