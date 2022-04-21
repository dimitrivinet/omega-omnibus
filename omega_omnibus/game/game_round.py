from omega_omnibus.game import game_manager, game_turn
from omega_omnibus.game import cards
from omega_omnibus.game.cards import Card, Rank, Suit


class Round:
    """A round of Omnibus is defined by the number of cards distributed to each player,
 that goes from 1 up to 12, and back to 1 for a total of 23 rounds.
 At the beginning of each Round, each player announce the number of turns they
 think they will win."""

    # First actions in the round
    trump: Card
    # Round Following
    current_round = int
    round_over: bool
    # Score Calculation
    player_tricks = int
    announced_tricks: int
    max_turns: int

    def __init__(self):
        # Trouver comment définir le nombre de tours
        self.current_round = {}
        self.max_turns = {}
        # définition de l'atout
        self.trump = []
        # Création d'un dict par joueur pour le suivi du score
        self.player_success = False
        self.tricks_count = 0
        self.announced_tricks = 0
        self.round_score = 0

    def turn_generation(self):
        """Generates a new turn."""
        # First define a Trump card
        self.trump = [Suit, Rank]
        # Then make each player announce, clockwise, and going one spot left
        # each time a round ends
        for player in game_manager.GameManager.players:
            if self.announced_tricks > self.max_turns:
                print("You cannot make more tricks than there is turns!")
            self.announced_tricks = ()

    def round_status(self):
        """Checks the advancement of the round and serves as a status for GameManager
        to go to next round."""
        if game_turn.Turn.turn_over is True:
            (self.current_round) = self.current_round + 1
        if self.max_turns == self.current_round:
            self.round_over = True

    # Réussi mais optimisable VVVVV

    def success_check(self,):
        """A player succeeds if the number of tricks he has made during the round
        is equal to the number of tricks this player announced."""
        # Utile pour les stats plus tard
        if self.announced_tricks == self.tricks_count:
            self.player_success = True

    def points_calculation(self):
        """The points a player makes or loses at the end of a turn depends on
        the number of tricks they announced compared to the number of tricks they made.
        """
    # A player that wins gains 10 points + the number of tricks that they announced
        if self.player_success is True:
            success_bonus = 10
            self.round_score = (success_bonus) + (self.announced_tricks)
    # A player that lost loses the dfference between what they announced and made.
        elif self.announced_tricks > self.tricks_count:
            self.round_score = (self.tricks_count) - (self.announced_tricks)
        elif self.announced_tricks < self.tricks_count:
            self.round_score = (self.announced_tricks)-(self.tricks_count)
