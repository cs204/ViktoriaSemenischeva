
import sys

if len(sys.argv) != 2:
    sys.exit("Слишком мало аргументов в командной строке")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Не python файл")

try:

    with open(filename, "r") as f:

        count = 0

        for line in f:

            cleaned_line = line.strip()

            if cleaned_line and not cleaned_line.startswith("#"):
                count += 1

    print(f"{count}")

except FileNotFoundError:
    sys.exit(f"Файл {filename} не найден.")
except Exception as e:
    sys.exit(f"Ошибка: {e}")