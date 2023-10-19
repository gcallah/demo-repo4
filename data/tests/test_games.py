import pytest

import data.games as gms


def test_get_games():
    games = gms.get_games()
    assert isinstance(games, dict)
    assert len(games) > 0
    for game in games:
        assert isinstance(game, str)
        assert isinstance(games[game], dict)
    assert gms.TEST_GAME_NAME in games


def test_add_game_dup_name():
    with pytest.raises(ValueError):
        gms.add_game(gms.TEST_GAME_NAME, 4)


def test_add_game_blank_name():
    with pytest.raises(ValueError):
        gms.add_game('', 4)


ADD_NAME = 'New Game'


def test_add_game():
    gms.add_game(ADD_NAME, 4)
    assert ADD_NAME in gms.get_games()
