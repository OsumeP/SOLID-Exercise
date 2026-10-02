from engine.track import Track


class Car:
    def __init__(self, name: str, speed: int, symbol: str = "\U0001F697"):
        self.name = name
        self.speed = speed
        self.symbol = symbol
        self.position = 0

    def move(self) -> None:
        self.position += self.speed
        

class RaceLogger:
    def __init__(self):
        self.entries = []

    def record(self, tick, racers):
        for racer in racers:
            self.entries.append(f"{racer.name}={tick}")
        
    def save(self, path="race_log.txt"):
        with open(path, "a", encoding="utf-8") as f:
            for entry in self.entries:
                f.write(entry)
                    

def main():
    cars = [Car("Red", 4), Car("Blue", 5), Car("Green", 3)]
    logger = RaceLogger()
    track = Track(length=30)
    track.run(cars, on_tick=logger.record)
    logger.save()


if __name__ == "__main__":
    main()
