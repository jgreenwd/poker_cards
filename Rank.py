from enum import IntEnum
from functools import total_ordering


@total_ordering
class Rank(IntEnum):
    STRAIGHT_FLUSH = 22
    FOUR_OF_A_KIND = 21
    FULL_HOUSE = 20
    FLUSH = 19
    STRAIGHT = 18
    THREE_OF_A_KIND = 17
    TWO_PAIR = 16
    ONE_PAIR = 15
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplementedError

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplementedError

    def __hash__(self):
        return hash(self.name)
