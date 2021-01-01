from Rank import Rank
from functools import total_ordering


class HandIterator:
    def __init__(self, hand):
        self._hand = hand
        self._index = 0

    def __next__(self):
        if self._index < (len(self._hand)):
            self._index += 1
            return self._hand[self._index - 1]
        raise StopIteration


@total_ordering
class Hand:
    def __init__(self, *args):
        self._cards = [] if len(args) == 0 else [arg for arg in args]
        self.value = self._set_value() if len(args) > 0 else None

    def __repr__(self):
        return ''.join([str(x) for x in self._cards if x is not None])

    def __str__(self):
        return ''.join([str(x) for x in self._cards if x is not None])

    def __iter__(self):
        return HandIterator(self._cards)

    def __getitem__(self, key=None):
        if not isinstance(key, int):
            raise TypeError
        if key > len(self._cards):
            raise IndexError
        if key is None:
            key = 0
        return self._cards[key]

    def __len__(self):
        return len(self._cards)

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError(f'Hands must have equal length.')

        # split ties
        if self.value == other.value:
            return self._cards == other.get_cards()

        return False

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError(f'Hands must have equal length.')

        # split ties
        if self.value == other.value:
            # test for Ace-low straight
            lo_self = (self._is_straight()) and (self[0].rank == Rank.ACE) and (self[1].rank == Rank.FIVE)
            lo_other = (other._is_straight()) and (other[0].rank == Rank.ACE) and (other[1].rank == Rank.FIVE)

            if lo_self and other.get_cards()[0].rank >= Rank.SIX:
                # print('self')
                return True
            elif lo_other and self._cards[0].rank >= Rank.SIX:
            #     print('other')
                return False

            # otherwise compare Ranks card by card (already sorted from _set_value)
            for a, b in zip(self, other):
                if a < b:
                    return True

        return self.value < other.value

    def get_cards(self):
        """ :return: reference to List of Cards in Hand """

        return self._cards

    def draw(self, card):
        """ Add a (Card) to the Hand

        :param card: (Card)
        """
        self._cards.append(card)  # add card to hand
        self.value = self._set_value()  # determine value

    def discard(self, index=0):
        """ Remove a (Card) from the Hand at given index (default 0)

        :param index: (Integer)
        :return: (Card)
        """
        try:
            card = self._cards.pop(index)
            self.value = self._set_value()
            return card

        except IndexError:
            raise IndexError

    def _is_straight(self):
        """ :return: True if Hand is a Straight """
        # straight == Ranks of n, n-1, n-2, n-3, n-4

        # test for Ace-Low Straight
        if ((self[0].rank == Rank.ACE) and (self[1].rank == Rank.FIVE) and (self[2].rank == Rank.FOUR)
                and (self[3].rank == Rank.THREE) and (self[4].rank == Rank.TWO)):
            return True

        return all((Rank(self[x].rank) == Rank(self[x + 1].rank + 1) for x in range(len(self) - 1)))

    def _is_flush(self):
        """ :return: True if Hand is a Flush """
        # flush == Suit(0) = Suit(1) .... = Suit(n)

        suit = self._cards[0].suit
        return all((card.suit == suit for card in self._cards[1:]))

    def evaluate_hand(self):
        """ :return: Rank of Hand """
        if len(self) == 0:
            return None

        if len(self) == 5:
            straight = self._is_straight()
            flush = self._is_flush()

            if straight and flush:
                return Rank.STRAIGHT_FLUSH
            elif flush:
                return Rank.FLUSH
            elif straight:
                return Rank.STRAIGHT

        # create a tuple of the ranks for each card in the hand
        ranks = tuple(self._cards.count(card) for card in self._cards)

        if 4 in ranks:
            return Rank.FOUR_OF_A_KIND
        elif 3 in ranks and 2 in ranks or ranks.count(3) >= 6:
            # 2nd condition covers hands with >5 Cards
            return Rank.FULL_HOUSE
        elif 3 in ranks:
            return Rank.THREE_OF_A_KIND
        elif 2 in ranks and ranks.count(2) >= 4:
            return Rank.TWO_PAIR
        elif 2 in ranks and ranks.count(2) == 2:
            return Rank.ONE_PAIR
        else:
            return self._cards[0].rank

    def _set_value(self):
        """ :return: Rank value of Hand """
        if len(self._cards) == 0:
            return None

        # Sort Cards in Hand by Rank, then by count
        self._cards = sorted(self._cards, reverse=True, key=lambda x: (self._cards.count(x), x.rank))

        # identify best possible 5-card hand from cards given
        # Flushes, Straights, & Straight-Flushes are only possible in Hands of 5 Cards
        # ie. no 6-card straights, just 2 straights in 1 hand eg. (2,3,4,5,6,7) == (2,3,4,5,6) and (3,4,5,6,7)
        # so, return the higher scoring combination
        if len(self._cards) <= 5:
            return self.evaluate_hand()
        else:
            from itertools import combinations

            combos = combinations(self._cards, 5)

            best_result = self._cards[0].rank

            for combo in combos:
                h = Hand(*combo)
                temp_result = Hand.evaluate_hand(h)

                if temp_result > best_result:
                    best_result = temp_result
                # add test for high card with equal results

            return best_result
