import contextlib
from enum import Enum, auto
import abc
from typing import Optional, Union
from numpy.linalg import lstsq
class FeeaderError(Exception):
    pass

class ClosedFeeder(FeeaderError):
    pass

class NotFood(FeeaderError):
    def __init__(self, food):
        self.food = food

class Animals(abc.ABC):
    @abc.abstractmethod
    def rob_feeder(self, feeder: "Feeder"):
        pass

class FeederState(Enum):
    OPEN = auto()
    CLOSE = auto()
    BROKEN = auto()

class Feeder:
    def __init__(self, food):
        self.food = food
        self.state = FeederState.CLOSE

    def get_food(self, food):
        if self.state == FeederState.OPEN:
            if food <= self.food:
                self.food -= food
                return food
            raise NotFood(self.food)
        elif self.state == FeederState.BROKEN:
            pass
        elif self.state == FeederState.CLOSE:
            raise ClosedFeeder()
        else:
            raise Exception("Unknown state")

    def __enter__(self):
        self.state = FeederState.OPEN

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.state = FeederState.CLOSE


class Dog(Animals):
    def rob_feeder(self, feeder: Feeder):
        request = 10
        while True:
            try:
                feeder.get_food(request)
                print("Hrum-Hrum")
                break
            except ClosedFeeder:
                print("Open feeder")
                feeder.state = FeederState.OPEN
            except NotFood as notFood:
                print("Not food")
                request = notFood.food
            finally:
                print("Gav-Gav")



class Cat(Animals):

    def rob_feeder(self, feeder: Feeder):
        try:
            feeder.get_food(20)
        except Exception:
            raise Exception("Meow-Meow")
@contextlib.contextmanager
def open_feeder(feeder):
    try:
        feeder.state = FeederState.OPEN
        yield feeder
    finally:
        feeder.state = FeederState.CLOSE

def main():
    feeder = Feeder(20)
    cat = Cat()
    dog = Dog()
    try:
        with feeder:
            dog.rob_feeder(feeder)
            cat.rob_feeder(feeder)
            dog.rob_feeder(feeder)
            dog.rob_feeder(feeder)
    except Exception:
        pass
    print(feeder.state)

    return 0


if __name__ == '__main__':
    main()
