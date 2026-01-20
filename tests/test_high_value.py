from lib.high_value import HighValue

def test_high_value():
    high_value_second_highest = HighValue(3, 7)
    assert high_value_second_highest.get_highest() == "Second value is higher"
    high_value_first_highest = HighValue(7, 3)
    assert high_value_first_highest.get_highest() == "First value is higher"
    high_value_equal = HighValue(3, 3)
    assert high_value_equal.get_highest() == "Values are equal"

def test_add():
    high_value_add_first = HighValue(2, 4)
    high_value_add_first.add(3, "first") 
    assert high_value_add_first.value_first == 5

    high_value_add_second = HighValue(1, 3)
    high_value_add_second.add(3, "second")
    assert high_value_add_second.value_second == 6

def test_add_get_higher():
    high_value_add_get_higher = HighValue(3, 1)
    high_value_add_get_higher.add(3, "second")
    assert high_value_add_get_higher.get_highest() == "Second value is higher"

def test_negative():
    high_value = HighValue(-1, -2)
    assert high_value.get_highest() == "First value is higher"
    high_value.add(-4, "first")
    assert high_value.value_first == -5
"""
def test_string():
    high_value = HighValue("a", 2)
    high_value.get_highest()
"""
def test_invalid_selection():
    high_value = HighValue(2, 2)
    high_value.add(4, "third") #does nothing
    assert high_value.value_first == 2
    assert high_value.value_second == 2
"""
Weird inputs:
negatives/zero
nothing - don't need to consider?
non-integer
add - invalid selection
add - negative
"""