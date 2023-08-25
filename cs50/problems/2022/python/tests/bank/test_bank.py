from bank import value

def main():
    test_hello()

def test_hello():

    assert value("Hello") == 0
    assert value("Hello, David") == 0

def test_init_h():

    assert value("How you doing?") == 20

def test_value():

    assert value("What's happening?") == 100