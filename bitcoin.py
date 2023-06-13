
import sys
import requests

try:
    n = float(sys.argv[1])
except ValueError:
    print("Аргумент командной строки не число")
    sys.exit()

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    json_data = response.json()
    current_price = float(json_data["bpi"]["USD"]["rate"].replace(",", ""))
except (requests.exceptions.RequestException, KeyError, ValueError):
    print("Пропущен аргумент командной строки")
    sys.exit()

price_n_btc = n * current_price
print("{:,.4f} USD".format(price_n_btc))