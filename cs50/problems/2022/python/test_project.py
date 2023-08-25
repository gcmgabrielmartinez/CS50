from project import present_value, maccauly_duration, modified_duration

def test_present_value():
    assert present_value() == 952.38
    assert present_value(yield_rate = .10) == 909.09
    assert present_value(maturity = 3) == 863.84
    assert present_value(yield_rate = .1076, coupon_rate = .1076, maturity = 10, paper = "Treasury Note") == 1000
    assert present_value(yield_rate = .1076, coupon_rate = .0498, maturity = 10, paper = "Treasury Note") == 660.22


def test_maccauly_duration():
    assert maccauly_duration() == 1
    assert maccauly_duration(yield_rate = .1025, maturity = 30, paper = "Treasury Note") == 9.94
    assert maccauly_duration(yield_rate = .08, coupon_rate = .071225, maturity = 3, paper = "Treasury Note") == 2.23

def test_modified_duration():
    assert modified_duration(yield_rate = .10, maturity = 30) == 27.27
    assert modified_duration(yield_rate = .1025, maturity = 30, paper = "Treasury Note") == 9.47
    assert modified_duration(yield_rate = .1025, coupon_rate = .095, maturity = 30, paper = "Treasury Note") == 9.3
