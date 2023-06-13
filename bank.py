
def main():

    greeting = input("Введите приветствие: ")

    print(value(greeting))

def value(greeting):

    if greeting.startswith("здравствуйте"):
        return 100

    elif greeting.startswith("з"):
        return 100

    else:
        return 100

if __name__ == "__main__":
    main()