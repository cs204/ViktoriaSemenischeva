def camel_to_snake(str, sep='_'):
    snake_register = ''
    for i in str:
        if i.isupper():
            snake_register += sep + i.lower()
        else:
            snake_register += i
    return snake_register.lstrip(sep)
camel_register = input("Верблюжий стиль: ")
print(camel_to_snake(camel_register))