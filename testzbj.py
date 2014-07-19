from unittest import TestCase, main
from zbj import Card, Hand, Deck

class CardBasics(TestCase):
    SUITS = ('C', 'S', 'H', 'D')
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class CardClass(TestCase):
    def test_type_of_instance(self):
        self.assertEqual(type(Card('C', 'A')), Card)

class CardSUITS(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'SUITS'))

    def test_should_have_the_four_card_suits(self):
        for suit in self.SUITS:
            self.assertTrue(suit in Card.SUITS)

class CardVALUES(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'VALUES'))

    def test_should_have_all_the_set_of_cards(self):
        for rank in self.VALUES.keys():
            self.assertTrue(rank in Card.VALUES)

    def test_ranks_should_have_correct_values(self):
        for rank in self.VALUES.keys():
            self.assertTrue(self.VALUES[rank] == Card.VALUES[rank])


class HandBasics(TestCase):
    pass


class DeckBasics(TestCase):
    pass


if __name__ == "__main__":
    main()
