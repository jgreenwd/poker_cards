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

        self._rank = Rank(rank)
        self._suit = suit.upper()

    def __repr__(self):
        """ Return representation of Card object """
        return f'{self.__class__.__name__}({self._rank}:{self._suit})'

    def __str__(self):
        """ Return 'spoken' version of card """
        if self._rank == Rank.ACE:
            rank = 'Ace'
        elif self._rank == Rank.JACK:
            rank = 'Jack'
        elif self._rank == Rank.QUEEN:
            rank = 'Queen'
        elif self._rank == Rank.KING:
            rank = 'King'
        else:
            rank = self._rank.value

        if self._suit == 'S':
            suit = 'Spades'
        elif self._suit == 'H':
            suit = 'Hearts'
        elif self._suit == 'C':
            suit = 'Clubs'
        else:
            suit = 'Diamonds'

        return f'<{rank:5} of {suit:8}> '

    def __eq__(self, other):
        return self._rank == other.get_rank()

    def __lt__(self, other):
        return self._rank < other.get_rank()

    def get_rank(self):
        """ Return value of Card's Rank """
        return self._rank

    def get_suit(self):
        """ Return value of Card's suit """
        return self._suit
