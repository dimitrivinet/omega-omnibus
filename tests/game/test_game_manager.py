# pylint: disable = missing-function-docstring
import copy
import random

import pytest

from omega_omnibus.game.cards import Card, Rank, Suit
from omega_omnibus.game.game_manager import FPC, GameManager

random.seed(42)


def random_card():
    """Create a random card."""

    suit = Suit(random.randint(1, 4))
    rank = Rank(random.randint(2, 14))

    return Card(suit, rank)


def test_fpc():
    assert FPC.to_enum("RANDOM") == FPC.RANDOM
    assert FPC.to_enum("FIRST_ADDED") == FPC.FIRST_ADDED
    assert FPC.to_enum("MANUAL") == FPC.MANUAL

    with pytest.raises(ValueError) as excinfo:
        FPC.to_enum("???")
        assert "Choice not found in enum." in excinfo.value


def test_create_manager():
    # pylint: disable = protected-access

    m = GameManager()
    assert m.players == {}
    assert m.rounds == []
    assert m.current_round_index == -1
    assert m.game_started is False
    assert m._players_frozen is False

    assert hasattr(m, "player_order") is False


def test_add_player():
    m = GameManager()
    m.add_player("1")
    assert len(m.players) == 1
    m.add_player("2")
    assert len(m.players) == 2

    m.freeze_players()
    m.start_game(first_player_choice="FIRST_ADDED")
    with pytest.raises(RuntimeError):
        m.add_player("3")


def test_freeze_players():
    m = GameManager()
    id1 = m.add_player("1")

    with pytest.raises(RuntimeError):
        m.freeze_players()

    id2 = m.add_player("2")
    m.freeze_players()

    assert m._players_frozen is True
    assert hasattr(m, "player_order") is True
    assert m.player_order == [id1, id2]


def test_create_current_round():
    # pylint: disable = protected-access

    m = GameManager()
    m.add_player("1")
    m.add_player("2")
    m.add_player("3")
    m.freeze_players()

    m.current_round_index = -3
    with pytest.raises(RuntimeError):
        m._create_current_round()

    m.current_round_index = 0
    m._create_current_round()
    assert len(m.rounds) == 1

    m.current_round_index += 1
    m._create_current_round()
    assert len(m.rounds) == 2

    with pytest.raises(RuntimeError):
        m._create_current_round()


def test_rotate_player_order():
    # pylint: disable = protected-access

    m = GameManager()
    m.add_player("1")
    m.add_player("2")
    m.add_player("3")

    m._rotate_player_order()

    m.freeze_players()
    m.start_game()  # create player order list
    base_order = m.player_order.copy()

    m._rotate_player_order()
    assert m.player_order[0] == base_order[1]

    m._rotate_player_order()
    assert m.player_order[0] == base_order[2]

    m._rotate_player_order()
    assert m.player_order[0] == base_order[0]

    m._rotate_player_order()
    assert m.player_order[0] == base_order[1]


def test_start_game():
    m = GameManager()

    with pytest.raises(RuntimeError) as excinfo:
        m.start_game()
        assert "Players must be frozen before starting game." in excinfo.value

    id1 = m.add_player("1")
    id2 = m.add_player("2")
    id3 = m.add_player("3")
    m.freeze_players()

    m1 = copy.deepcopy(m)
    m2 = copy.deepcopy(m)
    m3 = copy.deepcopy(m)
    m4 = copy.deepcopy(m)

    m1.start_game(first_player_choice="FIRST_ADDED")
    with pytest.raises(RuntimeError) as excinfo:
        m1.start_game(first_player_choice="FIRST_ADDED")
        assert "Game already started." in excinfo.value

    assert m1.player_order[0] == id1
    assert m1.game_started is True
    assert m1.current_round_index == 0

    with pytest.raises(RuntimeError) as excinfo:
        m2.start_game(first_player_choice="MANUAL")
        assert (
            " ".join(
                (
                    "Specified manual first player choice",
                    "but first player choice is not in players.",
                )
            )
            in excinfo.value
        )

    m3.start_game(first_player_choice="MANUAL", first_player=id2)
    assert m3.player_order[0] == id2

    m4.start_game(first_player_choice="RANDOM")
    assert m4.player_order[0] in [id1, id2, id3]


def test_next_round():
    m = GameManager()

    with pytest.raises(RuntimeError) as excinfo:
        m.next_round()
        assert "Game is not started!" in excinfo.value

    m.add_player("1")
    m.add_player("2")
    m.add_player("3")

    m.freeze_players()
    m.start_game()

    with pytest.raises(RuntimeError) as excinfo:
        m.next_round()
        assert "Current round is not over!" in excinfo.value

    m.set_trump(random_card())
    m.add_card(random_card())
    m.add_card(random_card())
    m.add_card(random_card())
    m.calculate_score()

    old_round_len = len(m.rounds)
    old_round_index = m.current_round_index
    ret = m.next_round()

    assert len(m.rounds) == old_round_len + 1
    assert m.current_round_index == old_round_index + 1
    assert ret is False

    while not m.over:
        m.set_trump(random_card())
        m.add_card(random_card())
        m.add_card(random_card())
        m.add_card(random_card())

        if not m.rounds[m.current_round_index].over:
            m.calculate_score()
            m.next_turn()
        else:
            m.calculate_score()
            m.next_round()

    ret = m.next_round()
    assert ret is True
