from um import count

def main():

    test_count()
    test_case_sense()
    test_spaces()

def test_count():

    assert count("um") == 1

def test_case_sense():

    assert count("Um... what are regular expressions") == 1
    assert count("Um, thanks, um, regular expressions make sense now") == 2

def test_spaces():

    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2