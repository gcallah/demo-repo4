import pytest

import data.games as gm


@pytest.fixture(scope='function')
def temp_game():
    name = gm._get_test_name()
    ret = gm.add_game(name, 0)
    yield name
    if gm.exists(name):
        gm.del_game(name)


def test_update_num_players(temp_game):
    NEW_NUM = 10
    gm.update_num_players(temp_game, NEW_NUM)
    updated_game = gm.get_game(temp_game)
    assert gm.get_num_players(updated_game) == NEW_NUM


def test_get_game(temp_game):
    game = gm.get_game(temp_game)
    assert isinstance(game, dict)


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


def test_get_games(temp_game):
    games = gm.get_games()
    assert isinstance(games, dict)
    assert len(games) > 0
    for game in games:
        assert isinstance(game, str)
        assert isinstance(games[game], dict)
    assert gm.exists(temp_game)


def test_add_game_dup_name(temp_game):
    """
    Make sure a duplicate game name raises a ValueError.
    `temp_game` is the name of the game that our fixture added.
    """
    with pytest.raises(ValueError):
        gm.add_game(temp_game, 4)


def test_add_game_blank_name():
    """
    Make sure a blank game name raises a ValueError.
    """
    with pytest.raises(ValueError):
        gm.add_game('', 4)


ADD_NAME = 'New Game'


def test_add_game():
    new_name = gm._get_test_name()
    ret = gm.add_game(new_name, 4)
    assert gm.exists(new_name)
    assert isinstance(ret, bool)
    gm.del_game(new_name)


def test_del_game(temp_game):
    name = temp_game
    gm.del_game(name)
    assert not gm.exists(name)


def test_del_game_not_there():
    name = gm._get_test_name()
    with pytest.raises(ValueError):
        gm.del_game(name)
