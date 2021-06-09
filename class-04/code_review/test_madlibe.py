from madlib import merge 

def test_read_template():
    pass

def test_merge():
    # text = "It was a {Adjective} and {Adjective} {Noun}."
    actual = merge("It was a {} and {} {}.", ['smart', 'cute', 'cat'])
    expected = "It was a smart and cute cat."
    assert actual == expected

