#wget https://cdn.cs50.net/python/2022/x/lectures/6/src6/names0.py
import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few comand-lines arguments")

    elif len(sys.argv) >2:
        sys.exit("Too many comand-lines arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    else:
        with open(sys.argv[1]) as file:
            lines = 0
            for line in file:
                if line.lstrip().startswith("#") or line.strip() == "" :
                    blockcomment = True
                else:
                    lines += 1
            print(lines, end ="")

except FileNotFoundError:
    sys.exit("File does not exist")
