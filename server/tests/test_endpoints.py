from http.client import OK, NOT_FOUND, FORBIDDEN, NOT_ACCEPTABLE, BAD_REQUEST

from unittest.mock import patch

import data.games as gm

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()


def test_hello():
    resp = TEST_CLIENT.get(ep.HELLO_EP)
    print(f'{resp=}')
    resp_json = resp.get_json()
    print(f'{resp_json=}')
    assert ep.HELLO_RESP in resp_json


def test_list_users():
    resp = TEST_CLIENT.get(ep.USERS_EP)
    assert resp.status_code == OK
    resp_json = resp.get_json()
    assert isinstance(resp_json, dict)
    assert ep.TITLE in resp_json
    assert ep.TYPE in resp_json
    assert ep.DATA in resp_json


def test_games_get():
    resp = TEST_CLIENT.get(ep.GAMES_EP)
    assert resp.status_code == OK
    resp_json = resp.get_json()
    assert isinstance(resp_json, dict)


@patch('data.games.add_game', side_effect=ValueError(), autospec=True)
def test_games_bad_add(mock_add):
    resp = TEST_CLIENT.post(ep.GAMES_EP, json=gm.get_test_game())
    assert resp.status_code == NOT_ACCEPTABLE


def test_games_add():
    resp = TEST_CLIENT.post(ep.GAMES_EP, json=gm.get_test_game())
    assert resp.status_code == OK
