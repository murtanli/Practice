class Worker:
    def __init__(self, name, last_name, surname):
        self.name = name
        self.last_name = last_name
        self.surname = surname

    def run(self):
        return str(f"{self.name} побежал")

    def walk(self):
        return str(f"{self.name} пошел")

    def talk(self, text):
        return str(f"{self.name} сказал {text}")

    def give_money(self, money, comy, spisok):
        if spisok[comy - 1]:
            spisok[comy - 1]["salary"] += money
            for worker_info in spisok:
                if (
                        worker_info["name"] == self.name
                        and worker_info["surname"] == self.last_name
                        and worker_info["patronymic"] == self.surname
                ):
                    worker_info["salary"] -= money
                    return str(f"Рабочий {self.name} отдал {money} рублей {spisok[comy - 1]['name']}")

        else:
            return str("Error")
        """name, surname, patronymic = comy.split(' ')

        for worker_info in spisok:
            if (
                    worker_info["name"] == name
                    and worker_info["surname"] == surname
                    and worker_info["patronymic"] == patronymic
            ):
                worker_info["salary"] += money
                print(f"Рабочий {self.name} отдал {money} рублей {comy}")
                break
        else:
            print(f"Работник {name} не найден в списке.")"""







