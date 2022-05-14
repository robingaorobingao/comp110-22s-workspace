"""List utility functions test file."""
__author__ = "730406932"

from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Edge case test for empty list."""
    evens: list[int] = []
    assert only_evens(evens) == []


def test_only_odds() -> None:
    """Use case test if there was only odd numbers."""
    evens: list[int] = [1, 3]
    assert only_evens(evens) == []


def test_only_evens_multiple() -> None:
    """Use case test if there was a mix of odd and even numbers."""
    evens: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(evens) == [2, 4]
    
    
def test_sub_empty() -> None:
    """Edge case for empty list."""
    subway: list[int] = []
    assert sub(subway, 0, 0) == []


def test_sub_single_item() -> None:
    """Use case if there was only one number."""
    subway: list[int] = [1]
    assert sub(subway, 0, 1) == [1]


def test_sub_multiple() -> None:
    """Use case if there multiple numbers."""
    subway: list[int] = [1, 2, 3, 4, 5]
    assert sub(subway, 1, 5) == [2, 3, 4, 5]


def test_concat_empty() -> None:
    """Edge case for empty lists."""
    list_tres: list[int] = []
    list_cuatro: list[int] = []
    assert concat(list_tres, list_cuatro) == []


def test_concat_partially_empty() -> None:
    """Use case for a single empty list."""
    list_tres: list[int] = [1, 2, 3, 4, 5]
    list_cuatro: list[int] = []
    assert concat(list_tres, list_cuatro) == [1, 2, 3, 4, 5]


def test_concat_partially_empty_again() -> None:
    """Use case for a single empty list."""
    list_tres: list[int] = []
    list_cuatro: list[int] = [1, 2, 3, 4, 5]
    assert concat(list_tres, list_cuatro) == [1, 2, 3, 4, 5]


def test_concat_unique_and_differing() -> None:
    """Two Lists of unique ints and differing lengths."""
    list_tres: list[int] = [1, 2, 3, 4, 5]
    list_cuatro: list[int] = [6, 7, 8, 9]
    assert concat(list_tres, list_cuatro) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_identical() -> None:
    """Use case for two identical lists."""
    list_tres: list[int] = [1, 2, 3, 4, 5]
    list_cuatro: list[int] = [1, 2, 3, 4, 5]
    assert concat(list_tres, list_cuatro) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def test_concat_unique_but_same() -> None:
    """Two Lists of unique ints of the same length."""
    list_tres: list[int] = [1, 2, 3, 4, 5]
    list_cuatro: list[int] = [6, 7, 8, 9, 0]
    assert concat(list_tres, list_cuatro) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]