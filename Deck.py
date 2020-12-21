from Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        """ Initialize the Deck and the Muck """
        self._deck = [Card(i, s) for i in Card.VALID_RANKS for s in Card.VALID_SUITS]
        self._muck = []
        self.shuffle()

    def __len__(self):
        return len(self._deck) + len(self._muck)

    def shuffle(self):
        """ Shuffle all cards in Deck and discard pile """
        for card in self._muck:
            self._deck.append(card)
        shuffle(self._deck)

    def deal(self):
        """ Select a Card from the top of the Deck """
        return self._deck.pop()

    def muck(self, card):
        """ Add Card to the muck pile """
        self._muck.append(card)
