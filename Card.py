from Rank import Rank
from functools import total_ordering


@total_ordering
class Card:
    """ Class representing any card from a standard 52-card deck """
    VALID_RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    VALID_SUITS = ('S', 'H', 'C', 'D')

    def __init__(self, rank, suit):
        if rank not in Card.VALID_RANKS:
            raise ValueError(f'Invalid rank: {rank}')
        if suit.upper() not in Card.VALID_SUITS:
            raise ValueError(f'Invalid suit: {suit}')

        self.rank = Rank(rank)
        self.suit = suit.upper()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.rank}:{self.suit})'

    def __str__(self):
        if self.suit == 'S':
            suit = 'Spades'
        elif self.suit == 'H':
            suit = 'Hearts'
        elif self.suit == 'C':
            suit = 'Clubs'
        else:
            suit = 'Diamonds'

        return f'<{str(self.rank)[5:].title():5} of {suit:8}> '

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank
