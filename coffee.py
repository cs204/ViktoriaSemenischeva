a = 50
b= 0

while b < a:
    print(f"Нужная сумма: {a - b}")
    coin = int(input("Вставьте монету: "))
    b += coin
   

print(f"Ваша сдача: {b - a}")