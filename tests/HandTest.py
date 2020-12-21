import unittest
from Hand import Hand
from Card import Card
from Deck import Deck
from Rank import Rank

deck = Deck()

test_hands = [
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(7, 'H')),     # 7 high [0]
    Hand(Card(7, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(7, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(8, 'H')),     # 8 high [3]
    Hand(Card(8, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(8, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(9, 'H')),     # 9 high [6]
    Hand(Card(9, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(9, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(10, 'H')),    # 10 high [9]
    Hand(Card(10, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(10, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(11, 'H')),    # Jack high [12]
    Hand(Card(11, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(11, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(12, 'H')),    # Queen high [15]
    Hand(Card(12, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(12, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(13, 'H')),    # King high [18]
    Hand(Card(13, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(13, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(14, 'H')),    # Ace high [21]
    Hand(Card(14, 'D'), Card(5, 'D'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S')),
    Hand(Card(14, 'H'), Card(6, 'H'), Card(4, 'C'), Card(3, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(2, 'S'), Card(3, 'C'), Card(4, 'H'), Card(5, 'H')),     # one pair [24]
    Hand(Card(5, 'D'), Card(4, 'D'), Card(3, 'S'), Card(2, 'C'), Card(2, 'H')),
    Hand(Card(6, 'H'), Card(4, 'H'), Card(3, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(2, 'S'), Card(3, 'C'), Card(3, 'H'), Card(4, 'H')),     # two pair [27]
    Hand(Card(4, 'D'), Card(3, 'D'), Card(3, 'S'), Card(2, 'C'), Card(2, 'H')),
    Hand(Card(5, 'H'), Card(3, 'H'), Card(3, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(2, 'S'), Card(2, 'C'), Card(3, 'H'), Card(4, 'H')),     # three of a kind [30]
    Hand(Card(4, 'D'), Card(3, 'D'), Card(2, 'S'), Card(2, 'C'), Card(2, 'H')),
    Hand(Card(5, 'H'), Card(3, 'H'), Card(2, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(3, 'S'), Card(4, 'C'), Card(5, 'H'), Card(6, 'H')),     # straight [33]
    Hand(Card(6, 'D'), Card(5, 'D'), Card(4, 'S'), Card(3, 'C'), Card(2, 'H')),
    Hand(Card(7, 'H'), Card(6, 'H'), Card(5, 'H'), Card(4, 'C'), Card(3, 'S')),
    Hand(Card(2, 'S'), Card(3, 'S'), Card(4, 'S'), Card(5, 'S'), Card(7, 'S')),     # flush [36]
    Hand(Card(7, 'C'), Card(5, 'C'), Card(4, 'C'), Card(3, 'C'), Card(2, 'C')),
    Hand(Card(7, 'S'), Card(6, 'S'), Card(4, 'S'), Card(3, 'S'), Card(2, 'S')),
    Hand(Card(2, 'D'), Card(2, 'S'), Card(2, 'C'), Card(3, 'H'), Card(3, 'S')),     # full house [39]
    Hand(Card(3, 'C'), Card(3, 'D'), Card(2, 'H'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(4, 'H'), Card(4, 'H'), Card(2, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(2, 'D'), Card(2, 'S'), Card(2, 'C'), Card(2, 'H'), Card(3, 'H')),     # four of a kind [42]
    Hand(Card(3, 'D'), Card(2, 'H'), Card(2, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(4, 'H'), Card(2, 'H'), Card(2, 'C'), Card(2, 'S'), Card(2, 'D')),
    Hand(Card(2, 'S'), Card(3, 'S'), Card(4, 'S'), Card(5, 'S'), Card(6, 'S')),     # straight flush [45]
    Hand(Card(6, 'H'), Card(5, 'H'), Card(4, 'H'), Card(3, 'H'), Card(2, 'H')),
    Hand(Card(7, 'S'), Card(6, 'S'), Card(5, 'S'), Card(4, 'S'), Card(3, 'S')),
    # 6 card hands
    Hand(Card(7, 'H'), Card(6, 'S'), Card(5, 'H'), Card(4, 'S'), Card(3, 'H'), Card(2, 'S')),  # str8 [48]
    Hand(Card(2, 'H'), Card(7, 'S'), Card(3, 'S'), Card(4, 'H'), Card(6, 'H'), Card(5, 'S')),
    Hand(Card(7, 'H'), Card(6, 'S'), Card(5, 'H'), Card(4, 'S'), Card(3, 'H'), Card(8, 'H')),
    Hand(Card(7, 'H'), Card(5, 'S'), Card(4, 'S'), Card(3, 'S'), Card(2, 'S'), Card(10, 'S')),  # flush [51]
    Hand(Card(7, 'S'), Card(5, 'H'), Card(4, 'H'), Card(3, 'H'), Card(2, 'H'), Card(10, 'H')),
    Hand(Card(7, 'H'), Card(9, 'S'), Card(4, 'S'), Card(3, 'S'), Card(2, 'S'), Card(10, 'S')),
    Hand(Card(7, 'S'), Card(8, 'S'), Card(9, 'S'), Card(5, 'S'), Card(6, 'S'), Card(10, 'S')),  # str8-fl [54]
    Hand(Card(7, 'H'), Card(8, 'H'), Card(9, 'H'), Card(5, 'H'), Card(6, 'H'), Card(10, 'H')),
    Hand(Card(7, 'S'), Card(8, 'S'), Card(9, 'S'), Card(11, 'S'), Card(5, 'S'), Card(10, 'S')),
    # 7 card hands
    Hand(Card(7, 'H'), Card(6, 'S'), Card(5, 'H'), Card(4, 'S'), Card(3, 'H'), Card(2, 'S'), Card(14, 'H')),  # str8
    Hand(Card(14, 'S'), Card(2, 'H'), Card(7, 'H'), Card(3, 'S'), Card(4, 'S'), Card(6, 'S'), Card(5, 'H')),
    Hand(Card(7, 'H'), Card(6, 'S'), Card(5, 'H'), Card(4, 'S'), Card(3, 'H'), Card(2, 'S'), Card(8, 'H')),
    Hand(Card(7, 'H'), Card(8, 'H'), Card(5, 'S'), Card(4, 'S'), Card(3, 'S'), Card(2, 'S'), Card(10, 'S')),  # flush
    Hand(Card(7, 'S'), Card(8, 'S'), Card(5, 'H'), Card(4, 'H'), Card(3, 'H'), Card(2, 'H'), Card(10, 'H')),
    Hand(Card(7, 'H'), Card(8, 'H'), Card(9, 'S'), Card(4, 'S'), Card(3, 'S'), Card(2, 'S'), Card(10, 'S')),
    Hand(Card(7, 'S'), Card(8, 'S'), Card(9, 'S'), Card(4, 'H'), Card(3, 'H'), Card(6, 'S'), Card(10, 'S')),  # str8-fl
    Hand(Card(7, 'H'), Card(8, 'H'), Card(9, 'H'), Card(4, 'S'), Card(3, 'S'), Card(6, 'H'), Card(10, 'H')),
    Hand(Card(7, 'S'), Card(8, 'S'), Card(9, 'S'), Card(11, 'S'), Card(3, 'H'), Card(5, 'H'), Card(10, 'S'))
]


class HandTest(unittest.TestCase):
    def test_constructor(self):
        hand = Hand()
        self.assertIsInstance(hand, Hand)

    def test_draw(self):
        hand = Hand()
        hand.draw(deck.deal())
        self.assertTrue(len(hand) == 1)

    def test_discard(self):
        hand = Hand()
        self.assertRaises(IndexError, hand.discard)
        hand.draw(deck.deal())
        card = hand.discard()
        self.assertTrue(len(hand) == 0)
        self.assertIsInstance(card, Card)

    def test_len(self):
        hand = Hand()
        self.assertTrue(len(hand) == 0)
        for i in range(1, 6):
            hand.draw(deck.deal())
            self.assertTrue(len(hand) == i)
        for i in range(4, -1, -1):
            hand.discard()
            self.assertTrue(len(hand) == i)
        self.assertTrue(len(hand) == 0)

    def test_value(self):
        # partial hands
        hand = Hand(Card(10, 'H'))
        self.assertEqual(hand.value, Rank.TEN)
        hand = Hand(Card(10, 'H'), Card(10, 'D'))
        self.assertEqual(hand.value, Rank.ONE_PAIR)
        hand = Hand(Card(2, 'D'), Card(2, 'C'), Card(3, 'D'), Card(3, 'C'))
        self.assertEqual(hand.value, Rank.TWO_PAIR)
        hand = Hand(Card(5, 'H'), Card(5, 'D'), Card(5, 'C'))
        self.assertEqual(hand.value, Rank.THREE_OF_A_KIND)
        hand = Hand(Card(7, 'H'), Card(7, 'D'), Card(7, 'C'), Card(7, 'S'))
        self.assertEqual(hand.value, Rank.FOUR_OF_A_KIND)

        # 5-card hands
        for i, j in enumerate(range(0, 46, 3)):
            self.assertEqual(test_hands[j].value, Rank(i + 7))
            self.assertEqual(test_hands[j + 1].value, Rank(i + 7))
            self.assertEqual(test_hands[j + 2].value, Rank(i + 7))

        # 6-card hands
        for i, j in enumerate(range(48, 51)):
            self.assertEqual(test_hands[j].value, Rank.STRAIGHT)
            self.assertEqual(test_hands[j+3].value, Rank.FLUSH)
            self.assertEqual(test_hands[j+6].value, Rank.STRAIGHT_FLUSH)

        # 7-card hands
        for i, j in enumerate(range(57, 60)):
            self.assertEqual(test_hands[j].value, Rank.STRAIGHT)
            self.assertEqual(test_hands[j+3].value, Rank.FLUSH)
            self.assertEqual(test_hands[j+6].value, Rank.STRAIGHT_FLUSH)

    def test_equal(self):
        for i in range(0, 64, 3):
            self.assertEqual(test_hands[i], test_hands[i + 1])
            self.assertNotEqual(test_hands[i], test_hands[i + 2])

    def test_less(self):
        for i in range(0, 45, 3):
            self.assertTrue(test_hands[i] < test_hands[i + 3])
        for i in range(48, 54, 3):
            self.assertTrue(test_hands[i] < test_hands[i + 3])
        for i in range(57, 63, 3):
            self.assertTrue(test_hands[i] < test_hands[i + 3])


if __name__ == '__main__':
    unittest.main()
