"""This is where you will implement your function skeletons and implementations below."""
__author__ = "730406932"


def invert(a: dict[str, str]) -> dict[str, str]:
    """The keys of the input list becomes the values of the output list and vice versa."""
    new: dict[str, str] = {}
    for key in a:
        if a[key] in new:
            raise KeyError("Oops! Duplicate keys/values detected!")
        else:
            new[a[key]] = key
    return new


def favorite_color(a: dict[str, str]) -> str:
    """It has one parameter, of type dict[str, str] of names and favorite colors. It returns a str which is the color that appears most frequently."""
    store: dict[str, int] = {}
    for name in a:
        if name in store:
            store[a[name]] += 1
        else:
            store[a[name]] = 1
    i: int = 0
    mode: str = ""
    for item in store:
        if i < store[item]:
            i = store[item]
            mode = str(item)
    return mode


def count(a: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    store: dict[str, int] = {} 
    # empty list
    for item in a:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store