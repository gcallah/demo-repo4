"""
games.py: the interface to our game data.
"""
import random

ID_LEN = 24
BIG_NUM = 100000000000000000000

MOCK_ID = '0' * ID_LEN

NAME = 'name'
NUM_PLAYERS = 'numPlayers'
TEST_GAME_NAME = 'Wizards Galore'

games = {
    'Dungeons and Dragons': {
        NUM_PLAYERS: 3,
    },
    TEST_GAME_NAME: {
        NUM_PLAYERS: 5,
    },
}


def _get_test_name():
    name = 'test'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def get_test_game():
    test_game = {}
    test_game[NAME] = _get_test_name()
    test_game[NUM_PLAYERS] = 0
    return test_game


def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


def get_games() -> dict:
    return games


def add_game(name: str, num_players: int) -> str:
    if name in games:
        raise ValueError(f'Duplicate game name: {name=}')
    if not name:
        raise ValueError('Game name may not be blank')
    games[name] = {NUM_PLAYERS: num_players}
    return _gen_id()


def get_name(game):
    return game.get(NAME, '')


def exists(name: str) -> bool:
    return name in get_games()
