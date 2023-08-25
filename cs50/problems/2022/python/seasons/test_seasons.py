from seasons import convert
import pytest

def main():

    test_convert()
 y   test_invalid()

def test_convert():

    assert convert("2022-08-03") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2023-08-02") == "One thousand, four hundred forty minutes"

def test_invalid():
    with pytest.raises(SystemExit): assert convert("January 8th, 2020") is SystemExit

