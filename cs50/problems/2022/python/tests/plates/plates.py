def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[:2].isalpha():
        return False
    char = 1
    for c in s[2:]:
        if not c.isalnum():
            return False
        if c.isnumeric() and char == 1 :
            char = 0
            if c == "0":
                return False
        if char == 0 and c.isalpha():
            return False
    return True

if __name__ == "__main__":
    main()