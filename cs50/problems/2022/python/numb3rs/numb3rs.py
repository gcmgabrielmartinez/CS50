import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$" , ip):
        for g in matches.groups():
            if int(g) > 255:
                return False
        return True

    else:
        return False

if __name__ == "__main__":
    main()