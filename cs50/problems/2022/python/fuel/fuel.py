
while True:
    try:
        num, den = map(int,input("Fraction: ").split("/"))

        if den == 0:
            raise ZeroDivisionError

        if den < 0 or num < 0 or num > den:
            raise ValueError

        frac = num/den*100

    except (ValueError, ZeroDivisionError):
        pass

    else:
        if frac >= 99  :
            print("F")
        elif frac <= 1 :
            print("E")
        else:
            print(f"{frac:.0f}%", end ="")
        exit()
