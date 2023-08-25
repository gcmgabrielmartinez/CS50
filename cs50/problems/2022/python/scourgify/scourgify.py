# wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

import csv
import sys

try:
    if len(sys.argv) < 3:
        sys.exit("Too few comand-lines arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many comand-lines arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        with open(sys.argv[1]) as file:
            before = csv.DictReader(file)
            with open(sys.argv[2], "w") as doc:
                after = csv.DictWriter(doc, fieldnames=["first", "last", "house"])
                after.writeheader()
                for student in before:
                    last, first = student["name"].split(",")
                    after.writerow(
                        {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": student["house"],
                        }
                    )

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
