from fuel import convert
from fuel import gauge
import pytest

def main():

    test_division_by_zero()
    test_value_error()
    test_outrange()
    test_fraction()

    test_gauge()
    test_full_gauge()
    test_empty_gauge()


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        convert("4/0")
    assert exc_info.type is ZeroDivisionError

def test_value_error():
    with pytest.raises(ValueError) as exc_info:
        convert("1.5/4")
    assert exc_info.type is ValueError

def test_outrange():
    with pytest.raises(ValueError) as exc_info:
        convert("5/4")
    assert exc_info.type is ValueError

def test_fraction():

    assert convert("3/4") == 75
    assert convert("2/3") == 67
    assert convert("1/3") == 33


def test_gauge():

    assert gauge(75) == "75%"
    assert gauge(67) == "67%"
    assert gauge(33) == "33%"

def test_full_gauge():

    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_empty_gauge():

    assert gauge(0) == "E"
    assert gauge(1) == "E"
