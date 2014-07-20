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
            self.assertIn(suit, Card.SUITS)


class CardVALUES(CardBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Card, 'VALUES'))

    def test_should_have_all_the_set_of_cards(self):
        for rank in self.VALUES.keys():
            self.assertIn(rank, Card.VALUES)

    def test_ranks_should_have_correct_values(self):
        self.assertDictEqual(self.VALUES, Card.VALUES)


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
        self.deck = Deck()


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

    def test_should_accept_a_card(self):
        self.assertIsNone(self.hand.add_card(Card('D', 'A')))

    def test_hand_lenght_gets_larger(self):
        befor_size = len(self.hand)
        self.hand.add_card(Card('S', 'A'))
        self.assertEqual(len(self.hand), befor_size + 1)


class HandGetValue(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, 'get_value'))

    def test_return_integer(self):
        self.assertEqual(type(self.hand.get_value()), int)

    def test_return_the_actual_value(self):
        local_hand = Hand()
        self.assertEqual(local_hand.get_value(), 0)
        local_hand.add_card(Card('C', '2'))
        self.assertEqual(local_hand.get_value(), 2)
        local_hand.add_card(Card('S', '9'))
        self.assertEqual(local_hand.get_value(), 11)

    def test_ace_has_speciall_value(self):
        local_hand = Hand()
        self.assertEqual(local_hand.get_value(), 0)
        local_hand.add_card(Card('S', 'A'))
        self.assertEqual(local_hand.get_value(), 11)
        local_hand.add_card(Card('H', 'T'))
        self.assertEqual(local_hand.get_value(), 11)


class HandHit(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, 'hit'))

    def test_should_accept_a_deck(self):
        self.assertIsNone(self.hand.hit(self.deck))


class HandBusted(HandBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Hand, 'busted'))

    def test_should_show_when_21_limit_is_passed(self):
        local_hand = Hand()
        self.assertFalse(local_hand.busted())
        local_hand.add_card(Card('S', 'T'))
        local_hand.add_card(Card('H', 'J'))
        local_hand.add_card(Card('D', '2'))
        self.assertTrue(local_hand.busted())


class DeckBasics(TestCase):
    def setUp(self):
        self.deck = Deck()


class DeckClass(TestCase):
    def test_type_of_instance(self):
        self.assertEqual(type(Deck()), Deck)


class DeckLenght(DeckBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Deck, '__len__'))

    def test_return_deck_length(self):
        self.assertEqual(len(self.deck), 52)


class DeckStr(DeckBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Deck, '__str__'))

    def test_return_a_string(self):
        self.assertEqual(type(self.deck.__str__()), str)


class DeckShuffle(DeckBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Deck, 'shuffle'))


class DeckDealCard(DeckBasics):
    def test_be_defined(self):
        self.assertTrue(hasattr(Deck, 'deal_card'))

    def test_should_return_a_card(self):
        self.assertEqual(type(self.deck.deal_card()), Card)


if __name__ == "__main__":
    main()
