from datetime import date
import sys
import re
import inflect

def main():
    print(convert(input("Day of Birth: ")), end="")

def convert(s):
    today = date.today()
    if day := re.search(r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<fh>\d{2})$", s):
        day_d = date(*map(int,day.groups()))
        delta = today - day_d
        write = inflect.engine()
        return (write.number_to_words(delta.days*24*60, andword ="" ).capitalize()+" minutes")
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()