import data.games as gm


def test_get_games():
    games = gm.get_games()
    assert isinstance(games, dict)
