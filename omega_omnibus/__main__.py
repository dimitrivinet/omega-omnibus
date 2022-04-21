from omega_omnibus.game.game_manager import GameManager  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    m = GameManager()

    while True:
        ret = input("Type player name to add (type 'q' to quit): ")
        if ret == "q":
            break

        if ret in ["default", "d"]:
            m.add_player("dimitri")
            m.add_player("yann")
            m.add_player("leah")
            m.add_player("clement")
            m.add_player("vincent")
            break

        m.add_player(ret)

    print(f"Players: {', '.join([player.name for player in m.players.values()])}")

    m.start_game(first_player_choice="RANDOM")
    print("Game started.")
    print(m.rounds)
    print([m.players[p_id].name for p_id in m.player_order])
