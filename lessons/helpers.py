"""Demonstrate defining a module imported elsewhere."""


# from numpy import power


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print("helpers.py was evaluated")