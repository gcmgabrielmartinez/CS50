import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if matches := re.search(r"^(?P<sh>\d{1,2})\:?(?P<sm>\d{2})? (?P<smer>PM|AM) to (?P<fh>\d{1,2})\:?(?P<fm>\d{2})? (?P<fmer>PM|AM)$", s):

            sh = convert_hour(matches.group("sh"), matches.group("smer"))
            #print(sh)
            sm = convert_minutes(matches.group("sm"))
            #print(sm)

            fh = convert_hour(matches.group("fh"), matches.group("fmer"))
            #print(fh)
            fm = convert_minutes(matches.group("fm"))
            #print(fm)

            return f"{sh:02}:{sm:02} to {fh:02}:{fm:02}"

        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")

def convert_hour(sh, mer):
    try:
        h = int(sh)
        if h > 12:
            raise ValueError
        elif h == 12:
            h -= 12

        if mer == "PM":
            return h + 12
        else:
            return h

    except ValueError:
        sys.exit("ValueError")

def convert_minutes(sm):
    try:
        if sm == None:
            return 0
        elif int(sm)<60:
            return int(sm)
        else:
            raise ValueError

    except ValueError:
        sys.exit("ValueError")


if __name__ == "__main__":
    main()