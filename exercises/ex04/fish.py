"""File to define Fish class."""


class Fish:

    def __init__(self, age=0):
        self.age = age

    def one_day(self):
        self.age += 1
