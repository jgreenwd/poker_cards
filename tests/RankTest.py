import unittest
from random import randint
from Rank import Rank


class RankTest(unittest.TestCase):
    def test_constructor(self):
        rank = Rank(randint(2, 14))
        self.assertIsInstance(rank, Rank)
        self.assertRaises(ValueError, Rank, 1)
        self.assertRaises(ValueError, Rank, 23)

    def test_same_value(self):
        rank1 = Rank(2)
        rank2 = Rank(2)
        self.assertEqual(rank1, rank2)
        self.assertGreaterEqual(rank1, rank2)
        self.assertLessEqual(rank1, rank2)
        self.assertFalse(rank1 > rank2)
        self.assertFalse(rank1 < rank2)
        self.assertFalse(rank1 != rank2)

    def test_diff_value(self):
        rank1 = Rank(2)
        rank2 = Rank(14)
        self.assertNotEqual(rank1, rank2)
        self.assertLess(rank1, rank2)
        self.assertLessEqual(rank1, rank2)
        self.assertGreater(rank2, rank1)
        self.assertGreaterEqual(rank2, rank1)
        self.assertFalse(rank1 == rank2)


if __name__ == '__main__':
    unittest.main()
