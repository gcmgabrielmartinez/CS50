import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        t = 1
        a = -1
        while a != (X+Y) and t<4:
            try:
                a = int(input(f"{X} + {Y} = "))
                if a != X+Y:
                    raise ValueError
            except ValueError:
                t += 1
                print("EEE")
                if t == 4:
                    print(f"{X} + {Y} = {X+Y}")
                pass
            else:
                score +=1
                break
    print(score)

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l in range(1,4):
                return l
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randrange(10)
    elif level == 2:
        return random.randrange(10,100)
    elif level == 3:
        return random.randrange(100,1000)


if __name__ == "__main__":
    main()