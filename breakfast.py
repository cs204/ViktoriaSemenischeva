
menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}

total_cost = 0

while True:
    try:
        dish = input("Блюдо: ").lower()

        if dish not in menu:
            continue

        total_cost += menu[dish]

    except EOFError:
        break

# Выводим суммарную стоимость заказа
print(f"\nСумма: {total_cost:.2f}" )