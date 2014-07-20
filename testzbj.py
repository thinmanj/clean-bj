import random
from unittest import TestCase, main
from zbj import Card, Hand, Deck

class CardBasics(TestCase):
    SUITS = ('C', 'S', 'H', 'D')
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

    def setUp(self):
        self.ac = Card('C', 'A')

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


class CardStr(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, '__str__'))

    def test_return_a_string(self):
        self.assertEqual(type(self.ac.__str__()), str)

    def test_random_string(self):
        self.assertEqual(str(self.ac), 'A(C)')


class CardGetSuit(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'get_suit'))

    def test_return_card_suit(self):
        self.assertEqual(self.ac.get_suit(), 'C')


class CardGetRank(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'get_rank'))

    def test_return_card_rank(self):
        self.assertEqual(self.ac.get_rank(), 'A')


class CardGetValue(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'get_value'))

    def test_return_card_value(self):
        self.assertEqual(self.ac.get_value(), 1)


class HandBasics(TestCase):
    def setUp(self):
        self.hand = Hand()
        self.ac = Card('C', 'A')
        self.hand.add_card(self.ac)


class HandClass(TestCase):
    def test_type_of_instance(self):
        self.assertEqual(type(Hand()), Hand)


class HandStr(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, '__str__'))

    def test_return_a_sting(self):
        self.assertEqual(type(self.hand.__str__()), str)

    def test_random_string(self):
        self.assertEqual(str(self.ac), 'A(C)')


class HandLenght(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, '__len__'))

    def test_return_a_int(self):
        self.assertEqual(type(self.hand.__len__()), int)


class HandAddCard(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, 'add_card'))
        

class DeckBasics(TestCase):
    pass


if __name__ == "__main__":
    main()
