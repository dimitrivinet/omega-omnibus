from . import global_instances


def pre_init() -> None:
    """This function is called before the server starts."""

    games_store = global_instances.games_store()
    games_store.load()
