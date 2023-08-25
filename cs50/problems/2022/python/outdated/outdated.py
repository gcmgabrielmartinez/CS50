months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        outdate = input("Date: ")
        if "/" in outdate:
            month, day, year = map(int,outdate.split("/"))
            if month > 12 or day >31:
                raise ValueError
            else:
                print(f"{year}-{int(month):02}-{int(day):02}", end="")
                print()
                exit()

        elif "," in outdate:
            date, year = outdate.split(",")
            month, day = date.split(" ")
            if months.index(month)+1 > 12 or int(day) >31:
                raise ValueError
            else:
                print(f"{year}-{months.index(month)+1:02}-{int(day):02}", end = "")
                print()
                exit()
    except ValueError:
        pass