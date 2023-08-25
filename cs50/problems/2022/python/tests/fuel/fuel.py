def main():

    frac = input("Fraction: ")
    perc = convert(frac)
    print(gauge(perc))

def convert(fraction):
    while True:
        try:
            num, den = map(int,fraction.split("/"))

            if den == 0:
                raise ZeroDivisionError

            if den < 0 or num < 0 or num > den:
                raise ValueError

            return int(round(num/den*100))

        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            pass

def gauge(percentage):
    if percentage >= 99  :
        return "F"
    elif percentage <= 1 :
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
