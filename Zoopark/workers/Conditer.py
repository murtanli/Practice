from .Worker import Worker

class Conditer(Worker):
    def __init__(self, name, last_name, surname):
        super().__init__(name, last_name, surname)
        self.name = name
        self.last_name = last_name
        self.surname = surname

    def cooking(self):
        return str(f"{self.name} Готовит печенья")

    def zarplata(self, zp):
        return str(f"{self.name} зарплата {zp}")