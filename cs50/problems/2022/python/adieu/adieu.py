# pip install inflect

import inflect

p = inflect.engine()
names = []
while True:
    try:
        name = input("Name: ").capitalize()
        names.append(name)

    except EOFError:
        print()
        print(f"Adieu, adieu, to {p.join(names) }")
        exit()
    else:
        pass
