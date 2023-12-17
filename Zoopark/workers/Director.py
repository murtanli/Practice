from .Worker import Worker


class Director(Worker):
    def __init__(self, name, last_name, surname):
        super().__init__(name, last_name, surname)
        self.name = name
        self.last_name = last_name
        self.surname = surname

    def talk(self, text):
        super().talk(text)
        return str(f"{self.name} наорал {text}")

    def give_salary(self, money, comy, spisok):
        if spisok[comy - 1]:
            spisok[comy - 1]["salary"] += money
        else:
            return str("Error")

    def mounth_salary(self, money_dir,money_work, spisok):
        for i in spisok:
            if i["role"] != "Director":
                i["salary"] += money_work
            else:
                i["salary"] += money_dir

    def premia(self):
        for i in self.spisok:
            if i["role"] != "Director":
                i["salary"] += 10000
        """name, surname, patronymic = comy.split(' ')

        for worker_info in spisok:
            if (
                    worker_info["name"] == name
                    and worker_info["surname"] == surname
                    and worker_info["patronymic"] == patronymic
            ):
                worker_info["salary"] += money
                print(f"Директор {self.name} выдал {money} рублей {comy}")
                break
        else:
            print(f"Работник {name} не найден в списке.")"""



