# pylint: disable = missing-function-docstring
import random

import pytest

from omega_omnibus.game.cards import Card, Rank, Suit
from omega_omnibus.game.game_round import Round

random.seed(42)

BASE_PLAYER_ID = "dummy"


def random_card():
    """Create a random card."""

    suit = Suit(random.randint(1, 4))
    rank = Rank(random.randint(1, 13))

    return Card(suit, rank)


def test_valid_round():
    r = Round(num_players=5)
    assert r.num_players == 5


def test_invalid_num_players():
    # num_players negative
    with pytest.raises(ValueError):
        _ = Round(num_players=-1)

    # num_players at 0
    with pytest.raises(ValueError):
        _ = Round(num_players=0)

    # num_players at 1
    with pytest.raises(ValueError):
        _ = Round(num_players=1)

    # invalid num_players type
    with pytest.raises(TypeError):
        _ = Round(num_players="3")


def test_set_trump():
    r = Round(num_players=5)
    trump = Card(Suit.CLUBS, Rank.TEN)
    r.set_trump(trump)

    assert r.trump == Card(Suit.CLUBS, Rank.TEN)


def test_set_trump_again():
    r = Round(num_players=5)
    r.set_trump(random_card())

    with pytest.raises(RuntimeError):
        r.set_trump(random_card())


def test_set_trump_notcard():
    r = Round(num_players=5)
    with pytest.raises(TypeError):
        r.set_trump("ace of spades!")  # type: ignore


def test_add_card():
    r = Round(num_players=3)
    r.set_trump(random_card())

    card = random_card()
    r.add_card(BASE_PLAYER_ID, card)

    assert r._dict == {BASE_PLAYER_ID: card}  # pylint: disable = protected-access


def test_add_card_wrong_type():
    r = Round(num_players=3)
    r.set_trump(random_card())

    with pytest.raises(TypeError):
        r.add_card(BASE_PLAYER_ID, "three of hearts")


def test_add_card_before_trump():
    r = Round(num_players=3)

    with pytest.raises(RuntimeError):
        r.add_card(BASE_PLAYER_ID, random_card())


def test_add_card_same_player():
    r = Round(num_players=3)
    r.add_card(BASE_PLAYER_ID, random_card())

    with pytest.raises(RuntimeError):
        r.add_card(BASE_PLAYER_ID, random_card())


def test_calculate_score():
    # basic win by score
    r1 = Round(num_players=4)
    r1.set_trump(Card(Suit.CLUBS, Rank.TEN))

    r1.add_card(f"{BASE_PLAYER_ID}1", Card(Suit.HEARTS, Rank.TEN))
    r1.add_card(f"{BASE_PLAYER_ID}2", Card(Suit.HEARTS, Rank.NINE))
    r1.add_card(f"{BASE_PLAYER_ID}3", Card(Suit.HEARTS, Rank.THREE))
    r1.add_card(f"{BASE_PLAYER_ID}4", Card(Suit.HEARTS, Rank.KING))

    assert r1.calculate_score() == f"{BASE_PLAYER_ID}4"

    # win with trump card
    r2 = Round(num_players=4)
    r2.set_trump(Card(Suit.CLUBS, Rank.TEN))

    r2.add_card(f"{BASE_PLAYER_ID}1", Card(Suit.HEARTS, Rank.TWO))
    r2.add_card(f"{BASE_PLAYER_ID}2", Card(Suit.HEARTS, Rank.ACE))
    r2.add_card(f"{BASE_PLAYER_ID}3", Card(Suit.CLUBS, Rank.ACE))
    r2.add_card(f"{BASE_PLAYER_ID}4", Card(Suit.DIAMONDS, Rank.THREE))

    assert r2.calculate_score() == f"{BASE_PLAYER_ID}3"

    # one omnibus
    r3 = Round(num_players=4)
    r3.set_trump(Card(Suit.CLUBS, Rank.TEN))

    r3.add_card(f"{BASE_PLAYER_ID}1", Card(Suit.HEARTS, Rank.ACE))
    r3.add_card(f"{BASE_PLAYER_ID}2", Card(Suit.HEARTS, Rank.TWO))
    r3.add_card(f"{BASE_PLAYER_ID}3", Card(Suit.HEARTS, Rank.ACE))
    r3.add_card(f"{BASE_PLAYER_ID}4", Card(Suit.DIAMONDS, Rank.THREE))

    assert r3.calculate_score() == f"{BASE_PLAYER_ID}2"

    # two omnibuses
    r4 = Round(num_players=6)
    r4.set_trump(Card(Suit.CLUBS, Rank.TEN))

    r4.add_card(f"{BASE_PLAYER_ID}1", Card(Suit.HEARTS, Rank.ACE))  # omnibus 1
    r4.add_card(f"{BASE_PLAYER_ID}2", Card(Suit.HEARTS, Rank.FOUR))  # winner
    r4.add_card(f"{BASE_PLAYER_ID}3", Card(Suit.HEARTS, Rank.ACE))  # omnibus 1
    r4.add_card(f"{BASE_PLAYER_ID}4", Card(Suit.HEARTS, Rank.QUEEN))  # omnibus 2
    r4.add_card(f"{BASE_PLAYER_ID}5", Card(Suit.HEARTS, Rank.QUEEN))  # omnibus 2
    r4.add_card(f"{BASE_PLAYER_ID}6", Card(Suit.HEARTS, Rank.THREE))  # omnibus 2

    assert r4.calculate_score() == f"{BASE_PLAYER_ID}2"


def test_calculate_score_error():
    r = Round(num_players=3)

    # trump card not set
    with pytest.raises(RuntimeError):
        r.calculate_score()

    # not all players have played
    r.add_card(f"{BASE_PLAYER_ID}", random_card())
    with pytest.raises(RuntimeError):
        r.calculate_score()