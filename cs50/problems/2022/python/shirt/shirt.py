#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
#wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
#unzip muppets.zip

import os
from PIL import Image
from PIL import ImageOps
import sys

try:
    if len(sys.argv) < 3:
        sys.exit("Too few comand-lines arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many comand-lines arguments")

    elif os.path.splitext(sys.argv[1])[1] not in [".jpg", ".jpeg", ".png" ]:
        print(os.path.splitext(sys.argv[1]))
        sys.exit("Invalid input")

    elif os.path.splitext(sys.argv[2])[1] not in [".jpg", ".jpeg", ".png" ]:
        print(os.path.splitext(sys.argv[2]))
        sys.exit("Invalid output")

    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and Output have different extensions")

    else:
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        after = ImageOps.fit(before, size)
        after.paste(shirt, shirt)
        after.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
