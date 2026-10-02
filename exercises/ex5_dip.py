from engine.track import Track


class SportsCar:
    symbol = "\U0001F3CE"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 6


class DeliveryVan:
    symbol = "\U0001F690"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3

class RocketSled:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.symbol = "\U0001F680"

    def move(self):
        self.position += 10

class Race:
    def __init__(self, racers, track = Track(length=30)):
        self.racers = racers
        self.track = track

    def start(self):
        return self.track.run(self.racers)


def main():
    roster1 = [RocketSled("Rocket1"), RocketSled("Rocket2"), SportsCar("Sports1")]
    Race(roster1, Track(length=30)).start()
    roster2 = [DeliveryVan("Deliver1"), RocketSled("Rocket1"), SportsCar("Sports1")]
    Race(roster2, Track(length=40)).start()


if __name__ == "__main__":
    main()
