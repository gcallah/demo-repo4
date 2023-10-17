import data.games as gm


def test_get_games():
    games = gm.get_games()
    assert isinstance(games, dict)
    assert len(games) > 0
    for game in games:
        assert isinstance(game, str)
        assert isinstance(games[game], dict)
