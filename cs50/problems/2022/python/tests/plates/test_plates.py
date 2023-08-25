from plates import is_valid

def main():
    test_size()
    test_char()
    test_num()

def test_size():
    assert is_valid("A") == False
    assert is_valid("ANA3387") == False
    assert is_valid("Abigail") == False
    assert is_valid("ANA247") == True

def test_char():
    assert is_valid("A12345") == False
    assert is_valid("AB1234") == True

def test_num():
    assert is_valid("AB247c") == False
    assert is_valid("ABC012") == False

def test_punc():
    assert is_valid("AB?234") == False
    assert is_valid("AB234.") == False

if __name__ == "__main__":
    main()

