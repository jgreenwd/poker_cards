import unittest
from Deck import Deck
from Card import Card


class DeckTest(unittest.TestCase):
    def test_constructor(self):
        deck = Deck()
        self.assertIsInstance(deck, Deck)

    def test_deal(self):
        deck = Deck()
        card = deck.deal()
        self.assertIsInstance(card, Card)

    def test_len(self):
        deck = Deck()
        self.assertTrue(len(deck) == len(Card.VALID_RANKS) * len(Card.VALID_SUITS))
        cards = [deck.deal() for _ in range(5)]
        self.assertTrue(len(deck) == len(Card.VALID_RANKS) * len(Card.VALID_SUITS) - len(cards))

    def test_muck(self):
        deck = Deck()
        cards = [deck.deal() for _ in range(5)]
        for _ in range(5):
            card = cards.pop()
            deck.muck(card)
            self.assertTrue(len(cards) + len(deck._muck) == 5)


if __name__ == '__main__':
    unittest.main()
