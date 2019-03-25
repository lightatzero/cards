## README.md

This read me file, uses reStructuredText format,
it includes doctest regression tests.

Tested on *ubuntu* with *python3* installed.

#The ``cards`` module

The module is used to illuminate the Python Data Model,
using examples from *fluent python* by Luciano Ramalho.


#Test
To run the doctests and unit tests: 
```Python
./test_cards
```

# Examples of usage
Import a deck as follows:
```Python
>>> import cards
>>> deck = cards.FrenchDeck()
>>>
```

Check the first and last card:
```Python
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>>
```

Print out all the cards:
```Python
>>> for card in reversed(deck): # doctest: +ELLIPSIS
...     print(card)  
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...
>>>
```

Check if cards exist:
```Python
>>> Card = cards.Card
>>> Card('Q', 'hearts') in deck
True
>>> Card('T', 'shows') in deck
False
>>> 
```
