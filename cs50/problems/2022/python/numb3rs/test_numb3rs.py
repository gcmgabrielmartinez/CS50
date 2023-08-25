from numb3rs import validate

def main():
    test_char()
    test_outrange()
    test_validate()

def test_char():

    assert validate("cat.255.255.255") == False
    assert validate("255.dog.255.255") == False
    assert validate("255.255.cro.255") == False
    assert validate("255.255.255.gif") == False

def test_outrange():

    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("1000.255.255.255") == False
    assert validate("255.255.255.255.1") == False


def test_validate():

    assert validate("2.2.2.2") == True
    assert validate("25.25.25.25") == True
    assert validate("255.255.255.255") == True
