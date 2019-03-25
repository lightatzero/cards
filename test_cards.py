#! /usr/bin/python3

import unittest
import cards


class TestFrenchDeck(unittest.TestCase):

    def setUp(self):
        self.deck = cards.FrenchDeck()

    def test_length(self):
        self.assertEqual(
                len(self.deck),
                52,
                'Deck is not correct size)')


if __name__ == '__main__':
    unittest.main()
