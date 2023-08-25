from working import convert
import pytest

def main():
    test_convert()
    test_nominutes()
    test_no_to()
    test_outrange()

def test_convert():

    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("09:30 AM to 05:30 PM") == "09:30 to 17:30"

def test_nominutes():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_no_to():
    with pytest.raises(ValueError) as exc_info:
        convert("12:00 AM  10:30 PM")
    assert exc_info.type is ValueError

def test_outrange():
    with pytest.raises(ValueError) as exc_info:
        convert("13:59 AM to 5:30 PM")
    assert exc_info.type is ValueError
