from .Worker import Worker
class Waiter(Worker):
    def __init__(self, name, last_name, surname):
        super().__init__(name, last_name, surname)
        self.name = name
        self.last_name = last_name
        self.surname = surname

    def spreads(self):
        return str(f"{self.name} приносит еду")

    def zarplata(self, zp):
        return str(f"{self.name} зарплата {zp}")

    def order(self):
        return str(f"{self.name} принимает заказ")

