from typing import Dict, List, Optional, Tuple

from omega_omnibus.game import cards
from omega_omnibus.game.game_turn import Turn


class Round:
    """Omnibus game round."""

    num_turns: int
    player_order: List[str]
    first_player: str

    score_dict: Dict[str, int]
    current_turn_index: int
    turns: List[Turn]

    _turn_winner: Optional[str]

    def __init__(self, num_turns: int, player_order: List[str]):
        """Create a round.

        player_order: list of player ids in order, with first player as element 0."""

        if num_turns < 1:
            raise ValueError("Number of turns can't be less than 1.")

        if len(player_order) < 2:
            raise ValueError("Can't play a round with less than two players.")

        self.num_turns = num_turns
        self.player_order = player_order.copy()

        self.score_dict = {player_id: 0 for player_id in player_order}
        self.current_turn_index = 0
        self.turns = [Turn(len(self.player_order)) for _ in range(self.num_turns)]

    def _rotate_player_order(self):
        """Rotate player order list to get the play order of current turn."""

        self.player_order.append(self.player_order.pop(0))

    def set_trump(self, trump: cards.Card):
        """Set trump card for the current turn."""

        if self.over:
            raise RuntimeError("Round is over.")

        self.turns[self.current_turn_index].set_trump(trump)

    def add_card(self, card: cards.Card):
        """Add new card to current turn."""

        if self.over:
            raise RuntimeError("Round is over.")

        self.turns[self.current_turn_index].add_card(self.current_player, card)
        self._rotate_player_order()

    def next_turn(self):
        """Start next turn. Returns True if the round is over, else False."""

        if not self.turns[self.current_turn_index].over:
            raise RuntimeError("Current turn is not over.")

        if not hasattr(self, "_turn_winner"):
            raise RuntimeError("calculate_score must be called before next_turn.")

        if not self.over:
            self.current_turn_index += 1

            # if last turn ended in a draw, set next player to last player to play
            if self._turn_winner is None:
                self._turn_winner = self.player_order[-1]

            # set next player to play to winner of last turn
            while self.current_player != self._turn_winner:
                self._rotate_player_order()

            delattr(self, "_turn_winner")

        return self.over

    def calculate_score(self) -> Tuple[Dict[str, int], bool]:
        """Get score for the turn. If the turn is over, returns True as the
        second value, else returns the temporary score and False."""

        # cannot calculate score for a turn that is not over, so return last
        # turn state
        if not self.turns[self.current_turn_index].over:
            return self.score_dict, self.over

        if hasattr(self, "_turn_winner"):
            raise RuntimeError("calculate_score must only be called once per turn.")

        self._turn_winner = self.turns[self.current_turn_index].calculate_score()
        if self._turn_winner is not None:
            self.score_dict[self._turn_winner] += 1

        return self.score_dict, self.over

    @property
    def current_player(self):
        """Player that is currently playing."""

        return self.player_order[0]

    @property
    def over(self) -> bool:
        """is round over."""

        return all(turn.over for turn in self.turns)


if __name__ == "__main__":  # pragma: no cover
    base_player_order = ["1", "2", "3", "4"]

    print("creating round")
    r = Round(3, base_player_order)

    print("setting trump card for turn 1")
    r.set_trump(cards.Card.from_string("two of hearts"))

    print("adding cards")
    to_play = "two of clubs"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "three of hearts"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "ten of clubs"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "ten of clubs"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))

    score = r.calculate_score()  # player 2 wins
    print(f"score: {score}")

    r.next_turn()
    print(f"winner: {r.current_player}")

    print("setting trump card for turn 2")
    r.set_trump(cards.Card.from_string("two of clubs"))

    print("adding cards")
    to_play = "three of hearts"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "two of clubs"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "three of hearts"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "two of clubs"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))

    score = r.calculate_score()  # equality
    print(f"score: {score}")

    r.next_turn()
    print("winner: none (equality)")

    print("setting trump card for turn 3")
    r.set_trump(cards.Card.from_string("two of diamonds"))

    print("adding cards")
    to_play = "three of diamonds"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "king of diamonds"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "king of diamonds"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))
    to_play = "two of diamonds"
    print(f"player {r.current_player} plays {to_play}")
    r.add_card(cards.Card.from_string(to_play))

    score = r.calculate_score()  # omnibus
    print(f"score: {score}")
