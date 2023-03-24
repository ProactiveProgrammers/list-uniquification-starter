"""Confirm that the functions in the uniquify module work correctly."""


from datauniquifier import uniquify

# TODO: Add docstrings that explain the purpose of each of these test cases


def test_unique_small_empty_set():
    list = []
    output = uniquify.unique_set(list)
    assert len(output) == 0


def test_unique_small_set_drop():
    list = ["1", "2", "1", "4", "5"]
    output = uniquify.unique_set(list)
    assert len(output) == 4


def test_unique_small_set_no_drop():
    list = ["1", "2", "10", "4", "5"]
    output = uniquify.unique_set(list)
    assert len(output) == 5
