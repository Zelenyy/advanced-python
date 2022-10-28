import abc
from contextlib import contextmanager
from enum import Enum, auto


class FeederError(Exception):
    pass


class CloseFeeder(FeederError):
    pass


class NoFood(FeederError):
    def __init__(self, food, message):
        self.food = food
        self.mesage = message


class HungryCatError(Exception):
    def __init__(self):
        pass


class FeederListener(abc.ABC):
    @abc.abstractmethod
    def invoke(self, feeder: "Feeder"):
        pass


class FeederObservable:
    def __init__(self):
        self.listeners = set()

    def subscribe(self, listener: FeederListener):
        self.listeners.add(listener)

    def send(self, feeder: "FeederObservable"):
        for listener in self.listeners:
            listener.invoke(feeder)


class FeederState(Enum):
    open = auto()
    close = auto()


class Feeder(FeederObservable):
    def __init__(self, food):
        super().__init__()
        self.food = food
        self.state = FeederState.close

    def open(self):
        self.state = FeederState.open
        self.send(self)

    def close(self):
        self.state = FeederState.close

    def get_food(self, food)-> int:
        if self.state != FeederState.open:
            raise CloseFeeder
        if food < self.food:
            self.food -= food
            return food
        raise NoFood(self.food, "Need more food, milord")


class Animals(abc.ABC):
    @abc.abstractmethod
    def rob_feeder(self, feeder: Feeder):
        pass


class Dog(Animals):

    def __init__(self):
        super().__init__()

    def rob_feeder(self, feeder: Feeder):
        try:
            feeder.get_food(20)
        except CloseFeeder:
            feeder.open()
        except NoFood as no_food:
            food = no_food.food
            feeder.get_food(food)
        finally:
            print("Gav-Gav")


class Cat(Animals, FeederListener):
    def rob_feeder(self, feeder: Feeder):
        try:
            feeder.get_food(10)
        except FeederError:
            raise HungryCatError

    def invoke(self, feeder: "Feeder"):
        self.rob_feeder(feeder)


@contextmanager
def open(feeder: Feeder):
    try:
        feeder.open()
        yield feeder
    finally:
        feeder.close()

def main():
    feeder = Feeder(60)
    cat = Cat()
    dog = Dog()

    feeder.subscribe(cat)
    try:
        cat.rob_feeder(feeder)
    except Exception:
        pass

    dog.rob_feeder(feeder)
    print(feeder.state)
    cat.rob_feeder(feeder)

    with open(feeder):
        dog.rob_feeder(feeder)

    print(feeder.state)

    try:
        with open(feeder):
            cat.rob_feeder(feeder)
    except HungryCatError:
        print("Angry Meow")

    print(feeder.state)
    return 0


if __name__ == '__main__':
    main()
