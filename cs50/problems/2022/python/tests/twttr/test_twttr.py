from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Twttr") == "Twttr"

    assert shorten("What's your name?") == "Wht's yr nm?"

    assert shorten("CS50") == "CS50"

    assert shorten("ALABAMA") == "LBM"


if __name__ == "__main__":
    main()
