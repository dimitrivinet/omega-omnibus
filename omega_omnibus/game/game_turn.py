from typing import Optional
from omega_omnibus.game.cards import Card, Suit, Rank


class Turn:
    """Represents a turn of Omnibus. Gets the trump card, the cards played
    during the turn in order, and compares the players cards value to calculate
    the winning player.

    \nIn a turn of Omnibus, each player plays a card once, clockwise.
    The first player determines the preferred card suit. A player has to play the
    preferred card suit if he can. Otherwise, he can choose to either play a
    trump card, or an other suit. """

    num_players: int
    winning_players: list
    cards_played: list
    _dict: dict
    trump: Card
    turn_over: bool
    turn_suit: Optional[Suit]

    def __init__(self, num_players: int):
        """Creates an empty turn. Must set trump card and add cards
        one by one."""
        self.num_players = num_players
        self.winning_players = []
        self._dict = {}
        # liste de suivi des cartes jouées dans l'ordre
        self.cards_played = []
        self.turn_suit = None
        self.turn_over = False

    def set_suit(self, suit: Suit):
        """Set the first played Suit of the turn."""

        if self.turn_suit is None:
            self.turn_suit = suit
        else:
            raise RuntimeError

    def add_card(self, player_id: str):
        """Add new card to turn."""

    def calculate_win(self):
        """Calculates winning player and returns winning player ID."""
        # The winning card of a turn is the highest 'value' card in the context
        # of the current turn
        if self.turn_over is True:
            winning_card = max(self.cards_played)
            self.winning_players.append()

    def _check_turn_over(self):
        """Checks if everything was set properly for calculating score."""
        if len(self.cards_played) == self.num_players:
            self.turn_over = True

    def card_value(self, card: Card):
        """Calculates the 'power' of a player's card in the current turn."""

        # la carte jouée en premier définis la couleur du tour
        # a donc une valeur plus haute qu'une carte normale
        # mais reste plus faible qu'un atout
        if len(self.cards_played) == 0:
            self.set_suit(card.suit)

        # si la carte jouée n'est pas jouée en premier et ne correspond pas
        # à la couleur demandée, sa valeur n'est utile qu'en cas d'omnibus
        # elle n'est donc pas multipliée
        bonus_value = 0

        # un atout joué a toujours une valeur plus élevée qu'une carte de base
        if card == self.trump:
            bonus_value = 28

        # si la carte n'est pas jouée en premier mais qu'elle correspond
        # à la couleur demandée, elle a une valeur égale à Rank+14
        elif card.suit == self.turn_suit:
            bonus_value = 14

        card_value = card.rank.value + bonus_value

        self.cards_played.append(card_value)
