import pytest

from omega_omnibus.game import cards


def test_from_string_cases():
    """Test from string function with different letter cases."""

    card_1 = cards.Card.from_string("ace of hearts")
    card_2 = cards.Card.from_string("ACE OF HEARTS")
    card_3 = cards.Card.from_string("Ace Of Hearts")

    assert card_1.rank == cards.Rank.ACE
    assert card_1.suit == cards.Suit.HEARTS
    assert card_2.rank == cards.Rank.ACE
    assert card_2.suit == cards.Suit.HEARTS
    assert card_3.rank == cards.Rank.ACE
    assert card_3.suit == cards.Suit.HEARTS


def test_from_string_invalid():
    """Test invalid card names."""

    with pytest.raises(ValueError):
        _ = cards.Card.from_string("twoofclubs")
    with pytest.raises(ValueError):
        _ = cards.Card.from_string("two clubs")
    with pytest.raises(ValueError):
        _ = cards.Card.from_string("two clubs")
    with pytest.raises(ValueError):
        _ = cards.Card.from_string("clubs of two")


def test_repr():
    """Test card repr."""

    card = cards.Card.from_string("ace of hearts")
    assert repr(card) == "Ace of Hearts"
