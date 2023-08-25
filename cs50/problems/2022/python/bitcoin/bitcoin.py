import json
import requests
import sys

try:
    if len(sys.argv) != 2:
        raise requests.RequestException
    n = float(sys.argv[1])

except requests.RequestException:
    sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Command-line argument is not a number")

else:
    bit_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(bit_price.json()) it is a dictionary of dictionaries!
    #print(json.dumps(bit_price.json(), indent=2))

    bp = bit_price.json()
    amount = n*bp["bpi"]["USD"]["rate_float"]
    print(f"${amount:,.4f}")
