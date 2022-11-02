import abc
from typing import Iterable


class Observer(abc.ABC):
    @abc.abstractmethod
    def make(self, old_value, new_value):
        pass

class Observable(abc.ABC):

    def __init__(self):
        self.listeners : Iterable[Observer] = set()

    def add_listeners(self, listener: Observer):
        self.listeners.add(listener)

    def print_x(self, x):
        print(x)

class Concrete(Observable):

    def print_x(self, x):
        x += 10
        super(Concrete, self).print_x(x)

    def __init__(self):
        super(Concrete, self).__init__()
        self._x = 0
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_value):
        for observer in self.listeners:
            observer.make(self.x, new_value)
        self._x = new_value

class Print(Observer):

    def make(self, old_value, new_value):
        print(old_value, new_value)

class RunTask(Observer):
    def make(self, old_value, new_value):
        pass


if __name__ == '__main__':
    a = Concrete()
    a.add_listeners(RunTask())
    a.add_listeners(Print())
    a.x = 10
    a.x = 20
    a.x = 30