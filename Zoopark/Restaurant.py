from workers.Powar import Powar
from workers.waiter import Waiter
from workers.Director import Director
from workers.Conditer import Conditer
import random

from accessify import protected, private


class Restaurant:
    def __init__(self, nums_workers, names):
        self._profit = 0
        self.nums_workers = nums_workers
        self.names = names
        self.employees = []

        self.menu = [
            ["pashtet", 120],
            ["iaishnitsa", 50],
            ["steik", 340],
            ["bread", 30],
            ["salyanka", 220],
            ["makarony", 40],
            ["grecha", 40],
            ["wok_s_kyroi", 120],
            ["wok_s_govadina", 150],
            ["pizza_margarita", 450],
            ["pizza_vegetarian", 550],
            ["pizza_ppeperoni", 550],
            ["pizza_4_sira", 350],
            ["FleurBurger_5000", 430000],
            ["Golden_Opulence_Sundae", 83000],
            ["Black_ikra_s_kyritsa", 12000]
        ]

    @protected
    def create_person(self, role, name, surname, patronymic):
        if role == "Director":
            return Director(name, surname, patronymic)
        elif role == "Powar":
            return Powar(name, surname, patronymic)
        elif role == "Waiter":
            return Waiter(name, surname, patronymic)
        elif role == "Conditer":
            return Conditer(name, surname, patronymic)
        else:
            raise ValueError("Invalid role")

    @protected
    def random_fio(self):
        fio = []
        for i in range(3):
            rn = random.randint(0, len(self.names[i]) - 1)
            fio.append(self.names[i][rn])
        return fio

    def add_employees(self):
        roles = ["Director", "Powar", "Waiter", "Conditer"]

        for i in range(len(roles)):
            for n in range(self.nums_workers[i]):
                fio = self.random_fio()
                # print(fio)
                #name = fio[0]
                #surname = fio[1]
                #patronymic = fio[2]
                employee = self.create_person(roles[i], fio[0], fio[1], fio[2])
                self.employees.append(
                    {
                        "class": employee,
                        "role": roles[i],
                        "name": fio[0],
                        "surname": fio[1],
                        "patronymic": fio[2],
                        "salary": 0
                    }
                )
                #self.employees.append(employee)
                #print(self.employees)


    def show_menu(self):
        num_blud = 0
        for i in self.menu:
            print(f"номер блюда - {num_blud} | наименование блюда - {i[0]}  | цена - {i[1]} рублей")
            num_blud += 1

    def order(self, nums_orders):
        order_price = 0
        for num in nums_orders:
            order_price += self.menu[num - 1][1]
        self.give_mounth_salary(order_price)
        return f"_______прибыль ресторана{self._profit}_______"
        # return int(order_price)

    @protected
    def give_mounth_salary(self, order_price):
        self._profit += round((order_price / 100) * 50)
        count_work = round((order_price - ((order_price / 100) * 75)) / (len(self.employees) - 1))
        sal_dir = round((order_price / 100) * 25)
        dir = Director(self.employees[0]['name'], self.employees[0]['surname'], self.employees[0]['patronymic'])

        dir.mounth_salary(sal_dir, count_work, self.employees)

        if self._profit % 10000 == len(self.employees) - 1:
            dir.premia()

        """for i in self.spisok:
            if i["role"] != "Director":
                i["salary"] += count_work
            else:
                i["salary"] += sal_dir"""

    def worker_output_info(self):
        return self.employees

