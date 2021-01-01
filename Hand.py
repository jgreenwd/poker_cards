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
            return self.get_cards() == other.get_cards()

        return False

    def __lt__(self, other):
        if len(self._cards) != len(other):
            raise ValueError(f'Hands must have equal length.')

        # split ties
        if self.value == other.value:
            # compare card Ranks (already sorted from _set_value)
            for a, b in zip(self.get_cards(), other.get_cards()):
                if a < b:
                    return True

            return False

        return self.value < other.value

    def get_cards(self):
        """ Get reference to Cards in Hand

        :return: List(...Cards) """
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
        if ((self[0].get_rank() == Rank.ACE) and (self[1].get_rank() == Rank.FIVE) and (self[2].get_rank() == Rank.FOUR)
                and (self[3].get_rank() == Rank.THREE) and (self[4].get_rank() == Rank.TWO)):
            return True

        return all((Rank(self[x].get_rank()) == Rank(self[x + 1].get_rank() + 1) for x in range(len(self) - 1)))

    def _is_flush(self):
        """ :return: True if Hand is a Flush """
        # flush == Suit(0) = Suit(1) .... = Suit(n)
        suit = self.get_cards()[0].get_suit()
        return all((card.get_suit() == suit for card in self.get_cards()[1:]))

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
        ranks = tuple(self.get_cards().count(card) for card in self.get_cards())

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
            return self.get_cards()[0].get_rank()

    def _set_value(self):
        """ Set value (Rank) of Hand

        :return: (Rank)
        """
        if len(self._cards) == 0:
            return None

        # Sort Cards in Hand by Rank, then by count
        self._cards = sorted(self.get_cards(), reverse=True, key=lambda x: (self.get_cards().count(x), x.get_rank()))

        # identify best possible 5-card hand from cards given
        if len(self.get_cards()) <= 5:
            return Hand._evaluate_hand(self)
        else:
            from itertools import combinations

            combos = combinations(self.get_cards(), 5)

            best_result = self.get_cards()[0].get_rank()

            for combo in combos:
                h = Hand(*combo)
                temp_result = Hand._evaluate_hand(h)

                if temp_result > best_result:
                    best_result = temp_result

            return best_result
