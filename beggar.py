import typing
import random


def load_cards(filename):
    out = []
    with open(filename) as f:
        for line in f:
            if len(out) == 0:
                out.append(int(line))
            else:
                out.append([("10" if i[0] == "X" else i[0], i[1]) for i in line.strip().split(",") if i != ""])
    return out


def save_cards(filename, cards):
    with open(filename, "w") as f:
        f.write(f"{cards[0]}\n")
        for hand in cards[1:]:
            f.write(",".join([("X" if c[0] == "10" else c[0]) + c[1] for c in hand]))
            f.write("\n")


def new_hands():
    hands = [0, []]
    cards = [(f"{i}", s) for i in range(2, 11) for s in "HCDS"]
    jacks = [("J", s) for s in "HCDS"]
    queens = [("Q", s) for s in "HCDS"]
    kings = [("K", s) for s in "HCDS"]
    aces = [("A", s) for s in "HCDS"]

    random.shuffle(cards)
    random.shuffle(jacks)
    random.shuffle(queens)
    random.shuffle(kings)
    random.shuffle(aces)

    for h in ["---K---Q-KQAJ-----AAJ--J--", "----------Q----KQ-J-----KA"]:
        hand = []
        for i in h:
            if i == "J":
                hand.append(jacks[0])
                jacks = jacks[1:]
            elif i == "Q":
                hand.append(queens[0])
                queens = queens[1:]
            elif i == "K":
                hand.append(kings[0])
                kings = kings[1:]
            elif i == "A":
                hand.append(aces[0])
                aces = aces[1:]
            else:
                assert i == "-"
                hand.append(cards[0])
                cards = cards[1:]
        hands.append(hand)
    return hands


def make_move(hands):
    player = hands[0]
    if len(hands[1]) > 0 and hands[1][-1][0] in "JQKA":
        ncards = 1 + "JQKA".index(hands[1][-1][0])
        cards = []
        for i in range(ncards):
            card = hands[2 + player][0]
            hands[2 + hands[0]] = hands[2 + player][1:]
            hands[1].append(card)
            cards.append(card)
            if card[0] in "JQKA":
                hands[0] = 1 - player
                return player, cards
        cards.append(("!", len(hands[1])))
        hands[3 - player] += hands[1]
        hands[1] = []
        hands[0] = 1 - player
        return player, cards
    else:
        card = hands[2 + player][0]
        hands[2 + hands[0]] = hands[2 + player][1:]
        hands[1].append(card)
        hands[0] = 1 - player
        return player, [card]


def card_name(card):
    names = {"A": "ace", "K": "king", "Q": "queen", "J": "jack"}
    if card in names:
        return names[card]
    return card


def suit_name(suit):
    names = {"H": "hearts", "C": "clubs", "D": "diamonds", "S": "spades"}
    if suit in names:
        return names[suit]
    raise ValueError(f"Unknown suit: {suit}")


def describe(player, cards):
    extra = ""
    if cards[-1][0] == "!":
        extra = f"\nPlayer {1 - player} picked up {cards[-1][1]} cards"
        cards = cards[:-1]
    cardnames = [f"the {card_name(c[0])} of {suit_name(c[1])}" for c in cards]
    if len(cardnames) > 2:
        cardnames = cardnames[:-2] + [cardnames[-2] + ", and " + cardnames[-1]]
    elif len(cardnames) == 2:
        cardnames = cardnames[:-2] + [cardnames[-2] + " and " + cardnames[-1]]
    return f"Player {player} played " + ", ".join(cardnames) + extra
