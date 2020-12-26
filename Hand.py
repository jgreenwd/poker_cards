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
            raise ValueError(f'Hands must have same length.')

        # split ties
        if self.value == other.value:
            # compare card Ranks (already sorted from _set_value)
            for a, b in zip(self.get_cards(), other.get_cards()):
                if a < b:
                    return True

            return False

        return self.value < other.value

    def get_cards(self):
        """ Return reference to Cards in Hand """
        return self._cards

    def draw(self, card):
        """ Add a Card to the Hand """
        self._cards.append(card)        # add card to hand
        self.value = self._set_value()  # determine value

    def discard(self, idx=0):
        """ Remove and Return a Card from the Hand """
        try:
            card = self._cards.pop(idx)
            self.value = self._set_value()
            return card

        except IndexError:
            raise IndexError

    @staticmethod
    def _is_straight(hand):
        # Return Boolean: is the current Hand a straight
        # straight == Ranks of n, n-1, n-2, n-3, n-4
        return all((Rank(hand[x].get_rank()) == Rank(hand[x + 1].get_rank() + 1) for x in range(len(hand)-1)))

    @staticmethod
    def _is_flush(hand):
        # Return Boolean: is the current Hand a flush
        suit = hand.get_cards()[0].get_suit()
        return all((card.get_suit() == suit for card in hand.get_cards()[1:]))

    @staticmethod
    def _evaluate_hand(hand):
        if len(hand) == 0:
            return None

        ranks = tuple(hand.get_cards().count(card) for card in hand.get_cards())

        if len(hand) == 5:
            straight = Hand._is_straight(hand)
            flush = Hand._is_flush(hand)

            if straight and flush:
                return Rank.STRAIGHT_FLUSH
            elif flush:
                return Rank.FLUSH
            elif straight:
                return Rank.STRAIGHT

        if 4 in ranks:
            return Rank.FOUR_OF_A_KIND
        elif 3 in ranks and 2 in ranks or ranks.count(3) == 6:
            return Rank.FULL_HOUSE
        elif 3 in ranks:
            return Rank.THREE_OF_A_KIND
        elif 2 in ranks and ranks.count(2) >= 4:
            return Rank.TWO_PAIR
        elif 2 in ranks and ranks.count(2) == 2:
            return Rank.ONE_PAIR
        else:
            return hand.get_cards()[0].get_rank()

    def _set_value(self):
        """ Return current Rank of Hand """
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
