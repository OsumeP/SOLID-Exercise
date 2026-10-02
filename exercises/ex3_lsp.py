import random

from engine.track import Track


class Vehicle:
    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class SteadyCar(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class UnreliableCar(Vehicle):
    symbol = "\U0001F699"

    def move(self) -> None:
        roll = random.random()
        if roll < 0.45:
            return
        else:
            self.position += 5


def main():
    vehicles = [SteadyCar("Reliable Rex"), UnreliableCar("Shaky Sam")]
    Track(length=30).run(vehicles)

if __name__ == "__main__":
    main()
