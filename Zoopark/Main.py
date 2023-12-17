from Restaurant import Restaurant
#from Manage_restaurant import Manage_restaurant



if __name__ == "__main__":
    spisok = []
    roles = {
        "Director": 1,
        "Powar": 5,
        "Waiter": 20,
        "Conditer": 2
    }
    names = [
        ["amir", "vladimir", "ira", "bulat", "kolya", "emil", "irek", "azat", "dima", "maria", "anya", "ilshat",
         "ryshan", "igor"], \
        ["muratov", "putin", "myhametzanov", "kazanov", "popyadlow", "kozynbaev", "kekow", "erzan", "sykhenko",
         "krakow", "ivanov", "shor"], \
        ["bulatovich", "renatovich", "albertovich", "ivanovich", "ignatiev", "alexsandrovich", "egorovich",
         "emilevich", "ryshanovich", "igorevich"]]
    for role, count in roles.items():
        num = int(input(f'input count {role} not more {count} - '))
        if count >= num > 0:
            spisok.append(num)
        else:
            print(f"error the entered number is greater or less than zero {role}")
            exit()
    restaurant = Restaurant(spisok, names)
    restaurant.add_employees()
    employees = restaurant.worker_output_info()
    while True:
        term_role = str(input("введите свою роль"))
        if term_role == "Director":
            print("Для взаимодействия с терминалом выберите действия "
                  "\n выдать зарплату - зп,\n выдать долг - долг,\n посмотреть всех рабочих- все, "
                  "\n посмотреть работника - пр ")
            ter = input()
            if ter == "зп":
                money = int(input("Введите зарплату - "))
                fio = int(input("Введите номер рабочего - "))
                employees[0]["class"].give_salary(money, fio, employees)
                restaurant.worker_output_info()
            elif ter == "долг":
                money = int(input("Введите сколько отдаете - "))
                fio = int(input("Введите свой номер рабочего - "))
                fio_dolg = int(input("Введите номер рабочего которому отдаете - "))
                employees[fio - 1]["class"].give_money(money, fio_dolg, employees)
                restaurant.worker_output_info()
            elif ter == "все":
                restaurant.worker_output_info()
            elif ter == "пр":
                num = int(input("введите номер рабочего - "))
                if num > 0:
                    print("________________________________________")
                    print(f"WORKER NUMBER - {num}")
                    print(f"class - {employees[num - 1]['class']}")
                    print(f"role - {employees[num - 1]['role']}")
                    print(f"name - {employees[num - 1]['name']}")
                    print(f"surname - {employees[num - 1]['surname']}")
                    print(f"surname - {employees[num - 1]['patronymic']}")
                    print(f"salary - {employees[num - 1]['salary']}")
                    print("________________________________________")
                    input("для продолжения введите любой символ")
                else:
                    print("номер введен не корректно")
            else:
                break
            #restaurant.simulate_day()
        elif term_role == "Guest":
            order = []
            count_blud = int(input("введите кол-во блюд"))
            restaurant.show_menu()
            restaurant.order(order)

            for _ in range(count_blud):
                num_blud = int(input("номер - "))
                order.append(num_blud)

            restaurant.order(order)
            inf = restaurant.worker_output_info()
            cout = 0
            print("________________________________________")
            for worker_info in inf:
                cout += 1
                print(f"WORKER NUMBER - {cout}")
                print(f"class - {worker_info['class']}")
                print(f"role - {worker_info['role']}")
                print(f"name - {worker_info['name']}")
                print(f"surname - {worker_info['surname']}")
                print(f"patronymic - {worker_info['patronymic']}")
                print(f"salary - {worker_info['salary']}")
                print("________________________________________")
        else:
            break

