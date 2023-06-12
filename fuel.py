def calculate_fuel_percentage():
    while True:
        try:
            # приглашение к вводу дроби
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split('/'))  # получение числителя и знаменателя
            if x > y or y == 0:
                print("Некорректный ввод. Попробуйте снова.")
                continue
            percentage = round((x / y) * 100 )  # вычисление процентов
            # проверка на пустой или полный бак
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(percentage, "%", sep = '' )
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
        except ZeroDivisionError:
            print("Деление на ноль. Попробуйте снова.")

# вызов функции для расчета степени заполненности бака
calculate_fuel_percentage()