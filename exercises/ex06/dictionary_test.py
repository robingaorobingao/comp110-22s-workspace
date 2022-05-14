"""For each function from below (invert, favorite_color, count), you are to define at least 3x unit test functions."""
__author__ = "730406932"

from dictionary import invert, count, favorite_color
import pytest


def test_invert_blank() -> None:
    """Edge case with blank input."""
    blank: dict[str, str] = {}
    assert invert(blank) == {}


def test_invert_key_and_value_are_the_same() -> None:
    """Use cases when the key and value are the same."""
    example = {"unc": "unc", "go heels": "go heels"}
    assert invert(example) == {"unc": "unc", "go heels": "go heels"}


def test_invert_key_and_value_are_different() -> None:
    """Use cases when the key and value are different."""
    example = {"unc": "go heels", "duke": "puke"}
    assert invert(example) == {"go heels": "unc", "puke": "duke"}


def test_invert_duplicate_values() -> None:
    """Use cases when two values are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_count_no_items() -> None:
    """Edge case when the list has no values."""
    example: list[str] = []
    assert count(example) == {}
    
    
def test_count_single_item() -> None:
    """Use case when the list only has one value."""
    example: list[str] = ["unc"]
    assert count(example) == {"unc": 1}


def test_count_many_items() -> None:
    """Use case when the list has many values."""
    example: list[str] = ["unc", "carolina", "unc"]
    assert count(example) == {"unc": 2, "carolina": 1}


def test_favorite_color_empty() -> None:
    """Edge case when the dictionary is empty."""
    example: dict[str, str] = {}
    assert favorite_color(example) == ""


def test_favorite_color_one_value() -> None:
    """Use case when the dictionary has one value."""
    example: dict[str, str] = {"Stuti": "blue"}
    assert favorite_color(example) == "blue"


def test_favorite_color_many_values() -> None:
    """Use case when the dictionary has many values."""
    example = {"Stuti": "blue", "roddy": "blue", "alana": "yellow", "robin": "green"}
    assert favorite_color(example) == "blue"