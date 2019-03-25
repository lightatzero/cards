The ``cards`` module
====================

This text file is using reStructuredText format.
This is a doctest based regression suite for cards.py
The aim is to investigate The Python Data Model.

python -m doctest -v test_cards.txt

>>> import cards
>>> Card = cards.Card
>>> deck = cards.FrenchDeck()
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')

>>> for card in reversed(deck): # doctest: +ELLIPSIS
...     print(card)  
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...

>>> Card('Q', 'hearts') in deck
True
>>> Card('T', 'shows') in deck
False
