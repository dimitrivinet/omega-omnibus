import copy

import pytest

from omega_omnibus.game.game_manager import FPC, GameManager


def test_fpc():
    assert FPC.to_enum("RANDOM") == FPC.RANDOM
    assert FPC.to_enum("FIRST_ADDED") == FPC.FIRST_ADDED
    assert FPC.to_enum("MANUAL") == FPC.MANUAL

    with pytest.raises(ValueError) as excinfo:
        FPC.to_enum("???")
        assert "Choice not found in enum." in excinfo.value


def test_create_manager():
    """Test basic creation and default values."""

    m = GameManager()
    assert m.players == {}
    assert m.rounds == []
    assert m.current_round_index == -1
    assert m.game_started is False


def test_add_player():
    """Test adding players."""

    m = GameManager()
    m.add_player("1")
    assert len(m.players) == 1
    m.add_player("2")
    assert len(m.players) == 2

    m.start_game(first_player_choice="FIRST_ADDED")
    with pytest.raises(RuntimeError):
        m.add_player("3")


def test_create_current_round():
    """Test round creation."""
    # pylint: disable = protected-access

    m = GameManager()
    m.add_player("1")
    m.add_player("2")
    m.add_player("3")

    m.current_round_index = -3
    with pytest.raises(RuntimeError):
        m._create_current_round(first_player="dummy_1")

    m.current_round_index = 0
    m._create_current_round(first_player="dummy_1")
    assert len(m.rounds) == 1

    m.current_round_index += 1
    m._create_current_round(first_player="dummy_1")
    assert len(m.rounds) == 2

    with pytest.raises(RuntimeError):
        m._create_current_round(first_player="dummy_1")


def test_rotate_player_order():
    """Test player order rotation."""

    m = GameManager()
    m.add_player("1")
    m.add_player("2")
    m.add_player("3")

    m._rotate_player_order()

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
    """Test game start function."""

    m = GameManager()

    with pytest.raises(RuntimeError) as excinfo:
        m.start_game()
        assert "Cannot play with less than 2 players." in excinfo.value

    id1 = m.add_player("1")
    with pytest.raises(RuntimeError) as excinfo:
        m.start_game()
        assert "Cannot play with less than 2 players." in excinfo.value

    id2 = m.add_player("2")
    id3 = m.add_player("3")

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

    m.start_game()

    with pytest.raises(RuntimeError) as excinfo:
        m.next_round()
        assert "Current round is not over!" in excinfo.value

    # ! TODO: next_round when round is over:

    # old_round_len = len(m.rounds)
    # old_round_index = m.current_round_index
    # m.next_round()

    # assert len(m.rounds) == old_round_len + 1
    # assert m.current_round_index == old_round_index + 1
