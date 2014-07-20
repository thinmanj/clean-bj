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
        self.clear()

    def __len__(self):
        return len(self.hand)

    def __str__(self):
        return ', '.join([str(card) for card in self.hand])
    
    def add_card(self, card):
        self.hand.append(card)
        if card.get_rank() == 'A':
            self.ace = True
        self.value += card.get_value()
        if self.value > 21:
            self.value = 0
            self.ace = 0
            raise Exception("Busted!")

    def get_value(self):
        if self.ace and self.value <= 10:
            return self.value + 10
        else:
            return self.value
    
    def hit(self, deck):
        card = deck.deal_card()
        print str(card)
        self.add_card(card)
        

    def busted(self):
        if self.get_value() > 21:
            return True

    def clear(self):
        self.hand = []
        self.ace = False
        self.value = 0


class Deck(object):
    def __init__(self):
        self.clear()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return ', '.join([str(card) for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def clear(self):
        self.deck = [Card(s, r) for s in Card.SUITS for r in Card.VALUES.keys()]
        self.shuffle()


class Game(object):
    def __init__(self):
        self.in_play = True
        self.player_chips = 100
        self.game_chips = 0
        self.deal()

    def __str__(self):
        if not self.in_play:
            return ""    
        return """
Game:
Game chips: %d
Dealer hand: %s
Player hand: %s
Player chips: %s
        """ % (self.game_chips, str(self.dealer), str(self.player), self.player_chips)

    def won(self):
        print "You won!"
        self.player_chips += 2 * self.game_chips
        self.game_chips = 0
        self.in_play = False

    def lost(self):
        print "You lost!"
        self.game_chips = 0
        self.in_play = False

    def tie(self):
        print "It's a tie!"
        self.player_chips += self.game_chips
        self.game_chips = 0
        self.in_play = False

    def deal(self, chips=1):
        if self.player_chips <= 0 or chips > self.player_chips:
            raise Exception("No enough chips.")
        self.in_play = True
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        self.player_chips -= chips
        self.game_chips = chips
        for x in range(2):
            self.dealer.hit(self.deck)
            self.player.hit(self.deck)

    def hit(self):
        if not self.in_play:
            return
        try:
            self.player.hit(self.deck)
        except Exception:
            self.in_play = False
            print "You went bust!"
            self.lost()
            raise Exception("Lost!")

        if self.player.get_value() == 21:
            print "Black Jack!"
            self.won()
            raise Exception("Won!")

    def stand(self):
        if not self.in_play:
            return

        while self.dealer.get_value() < 17 and self.in_play:
            try:
                self.dealer.hit(self.deck)
            except Exception:
                print "Dealer Busted!"
                self.in_play = False
    
        if self.player.get_value() > self.dealer.get_value():
            self.won()
        if self.player.get_value() < self.dealer.get_value():
            self.lost()
        else:
            self.tie()


def play():
    game = Game()
    try:
        while True:
            
            try:
                while True:
                    print str(game)
                    selection = raw_input("Do you whan to (h)it or to (s)tand: ")
                    if selection == "h":
                        game.hit()
                    elif selection == "s":
                        game.stand()
                        raise Exception
                    else:
                        print "Wrong selection..."
            except:
                selection_flag = True
                while selection_flag:
                    selection = raw_input("New (d)eal? or (e)xit: ")
                    if selection == "d":
                        game.deal(1)
                        selection_flag = False
                    elif selection == "e":
                        raise Exception
                    else:
                       print "Wrong selection..." 
    except:
        print "See you next time"


if __name__ == "__main__":
    play()
