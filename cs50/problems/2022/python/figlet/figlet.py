#pip install pyfiglet
import sys
import random
from pyfiglet import Figlet

try:
    figlet = Figlet()
    if len(sys.argv) == 1:
        f = random.choice(figlet.getFonts())
    elif sys.argv[1] in ["-f", "--font"]:
        f = sys.argv[2]
        if f not in figlet.getFonts():
            raise ValueError
    else:
        raise ValueError

except (ValueError, IndexError):
    sys.exit("Invalid usage")

else:
    figlet.setFont(font=f)
    s = input("Input: ")
    print(figlet.renderText(s))