
fruits_calories = {
    "Apple": 130,
    "Banana": 110,
    "Lime": 20,
    "Avocado": 61,
}


fruit = input("Фрукт: ")


if fruit in fruits_calories:
    print(f"Калории: {fruits_calories[fruit]}")



