"""Confirm that the functions in the analyze module work correctly."""


from datauniquifier import analyze

# TODO: Add docstrings that explain the purpose of each of these test cases


def test_half_reduction():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 2


def test_half_reduction_percentage():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 50


def test_small_reduction():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 1


def test_small_reduction_percentage():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 25


def test_no_reduction():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c", "d"]
    reduction = analyze.calculate_reduction(list_start, list_end)
    assert reduction == 0


def test_no_reduction_percentage():
    list_start = ["a", "b", "c", "d"]
    list_end = ["a", "b", "c", "d"]
    reduction = analyze.calculate_percent_reduction(list_start, list_end)
    assert reduction == 0
