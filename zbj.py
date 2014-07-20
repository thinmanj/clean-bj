import random


class Card(object):
    SUITS = ('C', 'S', 'H', 'D')
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

    def __init__(self, suit, rank):

        if (suit in self.SUITS) and (rank in self.VALUES.keys()):
            self.suit = suit
            self.rank = rank
            self.value = self.VALUES[rank]
        else:
            self.suit = None
            self.rank = None
            self.value = 0
            print "Invalid card: ", suit, rank

    def __str__(self):
        return "%s(%s)" % (self.rank, self.suit, )

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value


class Hand(object):
    def __init__(self):
        self.hand = []
        self.ace = False
        self.value = 0

    def __str__(self):
        return ', '.join([str(card) for card in self.hand])
    
    def add_card(self, card):
        self.hand.append(card)
        if card.get_rank() == 'A':
            self.ace = True
        self.value += card.get_value()

    def get_value(self):
        if self.ace and self.value <= 10:
            return self.value + 10
        else:
            return self.value
    
    def hit(self, deck):
        self.add_card(deck.deal_card())

    def busted(self):
        if self.get_value() > 21:
            return True


class Deck(object):
    def __init__(self):
        self.deck = [Card(s, r) for s in Card.SUITS for r in Card.VALUES.keys()]
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return ', '.join([str(card) for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


def deal():
    pass


def hit():
    pass


def stand():
    pass
