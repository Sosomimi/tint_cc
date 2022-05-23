from typing import List
from .utils import input_validator
from dataclasses import dataclass


class Stats:
    def __init__(self, data_list: List[int]) -> None:
        """
        Stats object initializer.
        """
        data_list.sort()
        self.data = data_list.copy()
        self.reversed = data_list.copy()
        self.reversed.reverse()
        self.ndict = dict()

        self.num_builder()


    def num_builder(self) -> None:
        """
        Generates a collection of custom objects that contains counters to their relative 
        position within the added numbers.
        """

        for num in self.data:
            index = self.data.index(num)
            index_rev = self.reversed.index(num)

            self.ndict[num] = AddedNumber(
                value=num,
                numbers_below=index, 
                numbers_above=index_rev,
                top_inclusive=len(self.data) - index_rev
            )


    @input_validator
    def less(self, input_num: int) -> int:
        """
        This method get the numbers less than the provided one.
        """
        self.validate_key(input_num)
        return self.ndict[input_num].numbers_below


    @input_validator
    def greater(self, input_num: int) -> int:
        """
        This method get the numbers greater than the provided one
        """
        self.validate_key(input_num)
        return self.ndict[input_num].numbers_above


    @input_validator
    def between(self, left_interval: int, right_interval: int) -> int:
        """"
        This method returns the numbers between the interval, including boundaries.
        """
        self.validate_key(left_interval)
        self.validate_key(right_interval)

        if right_interval < left_interval:
            left_interval, right_interval = right_interval, left_interval

        above = self.ndict[right_interval].top_inclusive
        below = self.ndict[left_interval].numbers_below

        return above - below


    def validate_key(self, input_num: int) -> None:
        try:
            self.ndict[input_num]
        except:
            raise KeyError(f'The provided number hasn\'t been added to the collection: {input_num}')


class DataCapture:
    def __init__(self) -> None:
        self.data = []

    @input_validator
    def add(self, input_num: int) -> None:
        self.data.append(input_num)


    def build_stats(self) -> Stats:
        return Stats(self.data)



@dataclass
class AddedNumber:
    value: int
    numbers_below: int
    numbers_above: int
    top_inclusive: int
