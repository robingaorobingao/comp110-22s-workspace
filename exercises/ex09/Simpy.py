"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730406932"


class Simpy:
    """Why do I need a docstring here when this was the skeleton I was given o_o ?"""
    values: list[float]
    # TODO: Your constructor and methods will go here.

    def __init__(self, arguments: list[float]):
        """Constructor definition for initialization of attributes."""
        self.values = arguments

    def __str__(self) -> str:
        """Define a method in Simpy named __str__ that takes no arguments and returns a str."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, int_number: int) -> None:
        """Its purpose is to fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < int_number:
            self.values.append(float_value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Its purpose is to fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        assert step != 0.0
        self.values = []
        while start != stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Its purpose is to compute and return the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The __add__ method should return a new Simpy object and should not mutate the object the method is called on."""
        new: list[float] = []
        if isinstance(rhs, float):
            for items in self.values:
                new.append(rhs + items)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for items in self.values:
                new.append(items + rhs.values[i])
                i += 1
        return Simpy(new)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """You will implement __pow__ much the same as __add__, except that the operation performed item-wise is exponentiation rather than addition."""
        new: list[float] = []
        if isinstance(rhs, float):
            for items in self.values:
                new.append(items ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for items in self.values:
                new.append(items ** rhs.values[i])
                i += 1
        return Simpy(new)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Next, you will add the ability to produce a mask, or a list[bool], based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        trew: list[bool] = []
        if isinstance(rhs, float):
            for items in self.values:
                trew.append(items == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for items in self.values:
                trew.append(items == rhs.values[i])
                i += 1
        return trew

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Next, you will add the ability to produce a mask, or a list[bool], based on the greater than relationship between each item in the values attribute with some other Simpy object or a float value."""
        trew: list[bool] = []
        if isinstance(rhs, float):
            for items in self.values:
                trew.append(items > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for items in self.values:
                trew.append(items > rhs.values[i])
                i += 1
        return trew

    # def __getitem__(self, rhs: int) -> float:
    #     """Next, you will add the ability to use the subscription operator with Simpy objects."""
    #     return self.values[rhs]

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """The big idea of the second usage of subscription notation is that if instead of giving an int inside the subscription brackets you give a list[bool], the expression will return a new Simpy object containing only the masked, or filtered, values."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            trew: list[float] = []
            i: int = 0
            for items in self.values:
                if rhs[i] is True:
                    trew.append(items)
                i += 1
            return Simpy(trew)