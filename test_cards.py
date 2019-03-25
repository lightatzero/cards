#! /usr/bin/python3

import unittest
import cards
import doctest


class TestFrenchDeck(unittest.TestCase):

    def setUp(self):
        self.deck = cards.FrenchDeck()
        self.card = cards.Card

    def test_length(self):
        self.assertEqual(
                len(self.deck),
                52,
                'Deck is not correct size')

    def test_spades_high(self):
        value = self.deck.spades_high(self.card('A', 'spades'))
        self.assertEqual(
                value,
                51,
                'ace of spades is not the highest value')

        value = self.deck.spades_high(self.card('2', 'clubs'))
        self.assertEqual(
                value,
                0,
                '2 of clubs is not the lowest value')


if __name__ == '__main__':
    doctest.testfile('README.md')
    print("Finished Doc tests, starting unit tests.")
    unittest.main()
