import data.games as gms


def test_get_games():
    games = gms.get_games()
    assert isinstance(games, dict)
    assert len(games) > 0
    for game in games:
        assert isinstance(game, str)
        assert isinstance(games[game], dict)
    assert gms.TEST_GAME_NAME in games
