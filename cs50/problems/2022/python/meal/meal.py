def main():
    c_clock = input("What time is it? ").strip()

    if " " in c_clock:
        c_clock, part = c_clock.split(" ")
    else:
       part = "UTC"

    n_clock = convert(c_clock)

    if part == "UTC":
        if 7 <= n_clock <= 8:
            print("breakfast time")
        elif 12 <= n_clock <= 13:
            print("lunch time")
        elif 18 <= n_clock <= 19:
            print("dinner time")
        else:
            exit()
    else:
        if 7 <= n_clock <= 8 and part == "a.m.":
            print("breakfast time")
        elif 0 <= n_clock <= 1 and part == "p.m.":
            print("lunch time")
        elif 6 <= n_clock <= 7 and part ==  "p.m.":
            print("dinner time")
        else:
            exit()

def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute)/60

if __name__ == "__main__":
    main()
