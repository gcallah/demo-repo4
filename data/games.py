"""
games.py: the interface to our game data.
"""

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


def get_games() -> dict:
    return games


def add_game(name: str, num_players: int):
    if name in games:
        raise ValueError(f'Duplicate game name: {name=}')
    if not name:
        raise ValueError('Game name may not be blank')
    games[name] = {NUM_PLAYERS: num_players}
