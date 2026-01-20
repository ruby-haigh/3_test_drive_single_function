from lib.count_words import * 

def test_count_words():
    assert count_words("one two three four five") == 5
    assert count_words("") == 0
