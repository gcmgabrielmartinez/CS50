from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError): assert Jar(-12) is ValueError


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError): jar.deposit(7) is ValueError

def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError): jar.withdraw(8) is ValueError
