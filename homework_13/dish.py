from abc import ABC, abstractmethod


class Dish(ABC):
    _name = ''

    def __init__(self, order):
        self._order = []

    @property
    def order(self):
        return self._order




