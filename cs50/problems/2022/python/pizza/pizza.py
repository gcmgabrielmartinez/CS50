#pip install tabulate
#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

import csv
from tabulate import tabulate
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few comand-lines arguments")

    elif len(sys.argv) >2:
        sys.exit("Too many comand-lines arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        with open(sys.argv[1]) as file:
            tab = csv.reader(file)
            print(tabulate(tab, headers = "firstrow", tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
