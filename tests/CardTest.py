import unittest
from random import choice, sample
from Card import Card


class CardTest(unittest.TestCase):
    def test_constructor(self):
        card = Card(7, 'H')
        self.assertIsInstance(card, Card)
        self.assertRaises(ValueError, Card, 2, 'J')
        self.assertRaises(ValueError, Card, 14, 'j')
        self.assertRaises(ValueError, Card, 1, 'H')
        self.assertRaises(ValueError, Card, 15, 'H')

    def test_same_rank(self):
        rank = choice(Card.VALID_RANKS)
        card1 = Card(rank, 'H')
        card2 = Card(rank, 'C')
        self.assertEqual(card1, card2)
        self.assertLessEqual(card1, card2)
        self.assertGreaterEqual(card1, card2)
        self.assertFalse(card1 != card2)
        self.assertFalse(card1 > card2)
        self.assertFalse(card1 < card2)

    def test_different_rank(self):
        card1 = Card(2, 'D')
        card2 = Card(14, 'S')
        self.assertNotEqual(card1, card2)
        self.assertLess(card1, card2)
        self.assertLessEqual(card1, card2)
        self.assertGreater(card2, card1)
        self.assertGreaterEqual(card2, card1)
        self.assertFalse(card1 == card2)

    def test_same_suit(self):
        suit = choice(Card.VALID_SUITS)
        card1 = Card(choice(Card.VALID_RANKS), suit)
        card2 = Card(choice(Card.VALID_RANKS), suit)
        self.assertEqual(card1.get_suit(), card2.get_suit())

    def test_different_suit(self):
        suits = sample(list(set(map(str.upper, Card.VALID_SUITS))), k=2)
        card1 = Card(choice(Card.VALID_RANKS), suits[0])
        card2 = Card(choice(Card.VALID_RANKS), suits[1])
        self.assertNotEqual(card1.get_suit(), card2.get_suit())


if __name__ == '__main__':
    unittest.main()
