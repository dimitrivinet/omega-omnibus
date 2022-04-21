# pylint: disable = missing-function-docstring
import random

import pytest

from omega_omnibus.game.cards import Card, Rank, Suit
from omega_omnibus.game.game_round import Round

random.seed(42)


def random_card():
    """Create a random card."""

    suit = Suit(random.randint(1, 4))
    rank = Rank(random.randint(2, 14))

    return Card(suit, rank)


def test_init():
    num_turns = 5
    player_order = ["1", "2", "3"]
    r = Round(num_turns, player_order)

    assert r.num_turns == num_turns
    assert r.player_order == player_order

    assert r.score_dict == {"1": 0, "2": 0, "3": 0}
    assert r.current_turn_index == 0
    assert len(r.turns) == num_turns

    assert r.current_player == "1"
    assert r.over is False


def test_init_invalid():
    with pytest.raises(ValueError):
        _ = Round(0, ["1", "2", "3"])

    with pytest.raises(ValueError):
        _ = Round(5, ["1"])


def test_rotate_player_order():
    # pylint: disable = protected-access

    r = Round(5, ["1", "2", "3"])

    assert r.player_order == ["1", "2", "3"]
    assert r.current_player == "1"

    r._rotate_player_order()
    assert r.player_order == ["2", "3", "1"]
    assert r.current_player == "2"

    r._rotate_player_order()
    assert r.player_order == ["3", "1", "2"]
    assert r.current_player == "3"


def test_next_turn():
    r = Round(3, ["1", "2"])

    with pytest.raises(RuntimeError):
        r.next_turn()

    r.set_trump(random_card())
    r.add_card(Card.from_string("eight of clubs"))
    r.add_card(Card.from_string("nine of clubs"))

    with pytest.raises(RuntimeError):
        r.next_turn()

    r.calculate_score()
    ret = r.next_turn()
    assert ret is False
    assert r.current_player == "2"  # 2 wins so he is the next player to play

    r.set_trump(random_card())
    card = random_card()
    r.add_card(card)
    r.add_card(card)

    r.calculate_score()
    ret = r.next_turn()
    assert ret is False
    assert r.current_player == "1"  # draw so last player plays again

    r.set_trump(random_card())
    r.add_card(random_card())
    r.add_card(random_card())

    r.calculate_score()
    ret = r.next_turn()
    assert ret is True


def test_calculate_score():
    # pylint: disable = protected-access

    r = Round(1, ["1", "2"])
    assert hasattr(r, "_turn_winner") is False

    ret = r.calculate_score()
    assert ret == ({"1": 0, "2": 0}, False)
    assert hasattr(r, "_turn_winner") is False

    r.set_trump(random_card())
    r.add_card(Card.from_string("six of hearts"))
    r.add_card(Card.from_string("five of hearts"))

    ret = r.calculate_score()
    assert ret == ({"1": 1, "2": 0}, True)

    with pytest.raises(RuntimeError):
        r.calculate_score()


def test_set_trump():
    r = Round(1, ["1", "2"])

    r.set_trump(Card(Suit.CLUBS, Rank.TEN))

    assert r.turns[r.current_turn_index].trump == Card(Suit.CLUBS, Rank.TEN)

    # set trump after round is over
    r.add_card(Card.from_string("two of hearts"))
    r.add_card(Card.from_string("three of hearts"))
    r.calculate_score()
    r.next_turn()

    with pytest.raises(RuntimeError):
        r.set_trump(Card(Suit.SPADES, Rank.KING))


def test_add_card():
    # pylint: disable = protected-access

    r = Round(1, ["1", "2"])

    r.set_trump(Card(Suit.CLUBS, Rank.TEN))

    r.add_card(Card.from_string("two of hearts"))
    assert "1" in r.turns[r.current_turn_index]._dict

    r.add_card(Card.from_string("three of hearts"))
    assert "2" in r.turns[r.current_turn_index]._dict

    r.calculate_score()
    r.next_turn()

    with pytest.raises(RuntimeError):
        r.add_card(Card.from_string("three of hearts"))
