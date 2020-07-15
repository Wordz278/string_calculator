from string_calculator.calculator import add, negatives_not_allowed
import pytest


def test_add_empty_str():
    assert add("") == 0


def test_add_one_number():
    assert add("1") == 1


def test_add_two_numbers():
    assert add("1,2") == 3


def test_add_many_numbers():
    assert add("1,2,3,4") == 10


def test_new_lines():
    assert add("1\n2,3") == 6


def test_diff_delimiters():
    assert add("//;\n1;2") == 3


def test_negatives_not_allowed():
    with pytest.raises(ValueError, match=r"[-1, -2]"):
        add("-1,-2,3,4")
