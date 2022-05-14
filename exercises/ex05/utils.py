"""List utility functions."""
__author__ = "730406932"


def only_evens(evens: list[int]) -> list[int]:
    """Given a list of ints, only_evens should return a list containing only the elements of the input list that were even."""
    new: list[int] = []
    i: int = 0
    while i < len(evens):
        if evens[i] / 2 == evens[i] // 2:
            new.append(evens[i])
        i += 1
    return new


def sub(subway: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1. This function should not mutate its input list."""
    new: list[int] = []
    if start < 0:
        start = 0
    if end > len(subway):
        end = len(subway)
    elif len(subway) == 0 or start > len(subway) or end <= 0:
        return subway
    elif start == len(subway):
        return list()
    while start < end:
        new.append(subway[start])
        start += 1
    return new


def concat(list_uno: list[int], list_dos: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    # i: int = 0
    # while i < len(list_dos):
    #     list_uno.append(list_dos[i])
    #     i += 1
    for numbers in list_dos:
        list_uno.append(numbers)
    return list_uno