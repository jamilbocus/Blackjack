#     Requirements:
# The game should recognise an ace as high or low depending on what is best for the player;
# The house should be an automated player but other players, up to 4,
# should be humans operating a command line interface;
# The house should win all ties;
# It is possible for more than one player to win a hand;
# Must be able to stick and twist
# Must have an autonomous dealer
# Dealer starts by showing only a single card
# All Players are dealt two cards to start
# Extra marks will be awarded for tests, good function/variable names,
# sensible comments/docstrings, clean Pythonic code
# The following are out of scope:
# Insurance rule
# Keep track of currency
# Implement the split rule.

import random

def get_deck():
    deck = [value + ' of ' + suit for value in '23456789TJQKA' for suit in 'SHDC']
    random.shuffle(deck)
    return iter(deck)

cards = get_deck()
print(next(cards))
print(next(cards))