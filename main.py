from Deck import Deck
from Hand import Hand

deck = Deck()


def Texas_HoldEm():
    hand1 = Hand()
    hand2 = Hand()
    hand3 = Hand()
    hand4 = Hand()

    for _ in range(2):
        hand1.draw(deck.deal())
        hand2.draw(deck.deal())
        hand3.draw(deck.deal())
        hand4.draw(deck.deal())

    # flop
    deck.deal()
    card1 = deck.deal()
    deck.deal()
    card2 = deck.deal()
    deck.deal()
    card3 = deck.deal()

    # turn
    deck.deal()
    card4 = deck.deal()

    # river
    deck.deal()
    card5 = deck.deal()

    for i in range(1, 5):
        eval(f"hand{i}.draw(card1)")
        eval(f"hand{i}.draw(card2)")
        eval(f"hand{i}.draw(card3)")
        eval(f"hand{i}.draw(card4)")
        eval(f"hand{i}.draw(card5)")

    hands = sorted([hand1, hand2, hand3, hand4], reverse=True, key=lambda x: (x.value, [y.get_rank() for y in x.get_cards()]))

    for hand in hands:
        print(hand.value, '\t', hand)

    print()
    print(max(hands))


Texas_HoldEm()
