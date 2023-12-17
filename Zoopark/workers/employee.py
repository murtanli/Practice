from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def talk(self, text):
        pass

    @abstractmethod
    def give_money(self, amount, recipient):
        pass
