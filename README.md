# Poker_Cards
Python Poker Cards for Flask backend<br>

This repository is designed to randomly create and evaluate hands of _n-_ size (1 <= _n-_ <= 7). Evaluations are based on standard poker hands with no wildcards:

__Hands__:<br>
- _Straight Flush_
- _4 of a Kind_
- _Full House_
- _Flush_
- _Straight_
- _3 of a Kind_
- _2 Pair_
- _1 Pair_
- _High Card_
<br><br>
__Classes__:<br>
- __Rank__ - Ordering of card/hand values; used to select winner
- __Card__ - Basic unit of game play; can represent any value in a standard 52-card deck
- __Hand__ - Combination of Cards; For hands larger than 5, Texas Hold'Em rules are applied (best 5-card hand out of all in hand)
- __Deck__ - Mechanism for creating, shuffling, dealing, and collecting cards
