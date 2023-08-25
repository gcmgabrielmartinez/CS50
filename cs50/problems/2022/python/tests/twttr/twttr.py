def main():
    name = input("Input: ").strip()
    tt_name = shorten(name)
    print(f"Output: {tt_name}")

def shorten(word):
    tt_word = str()
    for c in word:
        if c.lower() not in ["a","e","i","o","u"]:
            tt_word += c

    return tt_word

if __name__ == "__main__":
    main()