import pytest

import data.games as gm


@pytest.fixture(scope='function')
def temp_game():
    name = gm._get_test_name()
    ret = gm.add_game(name, 0)
    return name
    # delete the game!


def test_get_test_name():
    name = gm._get_test_name()
    assert isinstance(name, str)
    assert len(name) > 0


def test_gen_id():
    _id = gm._gen_id()
    assert isinstance(_id, str)
    assert len(_id) == gm.ID_LEN


def test_get_test_game():
    assert isinstance(gm.get_test_game(), dict)


def test_get_games():
    games = gm.get_games()
    assert isinstance(games, dict)
    assert len(games) > 0
    for game in games:
        assert isinstance(game, str)
        assert isinstance(games[game], dict)
    assert gm.TEST_GAME_NAME in games


def test_add_game_dup_name(temp_game):
    """
    Make sure a duplicate game name raises a ValueError.
    """
    dup_name = temp_game
    with pytest.raises(ValueError):
        gm.add_game(dup_name, 4)


def test_add_game_blank_name():
    """
    Make sure a blank game name raises a ValueError.
    """
    with pytest.raises(ValueError):
        gm.add_game('', 4)


ADD_NAME = 'New Game'


def test_add_game():
    ret = gm.add_game(ADD_NAME, 4)
    assert gm.exists(ADD_NAME)
    assert isinstance(ret, str)
