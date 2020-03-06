from string_calculator.calculator import Calculator
calculator = Calculator()


def test_add_empty_str():
    assert calculator.add("") == 0


def test_add_one_number():
    assert calculator.add("1") == 1


def test_add_two_numbers():
    assert calculator.add("1,2") == 3


def test_add_many_numbers():
    assert calculator.add("1,2,3,4") == 10


def test_new_lines():
    assert calculator.add("1\n2,3") == 6


def test_diff_delimiters():
    assert calculator.add("//;\n1;2") == 3


# def test_check_negatives():
#     with pytest.raises(Exception) as err:
#         assert calculator.add("//;\n-1;2,-3")
#         assert str(err.value) == "Negatives not allowed: -1,-3,"


def test_more_than_twenty():
    assert calculator.add("//;\n1;2") == 3


# def test_delimeter_len():
#     assert calculator.add("//[***]\n1***2***3") == 6


# def test_multiple_delimeters():
#     assert calculator.add("//[*][%]\n1*2%3") == 6
