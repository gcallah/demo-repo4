"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields
from flask_cors import CORS

import werkzeug.exceptions as wz

import data.games as gm
import data.users as users

app = Flask(__name__)
CORS(app)
api = Api(app)

DELETE = 'delete'
DEFAULT = 'Default'
MENU = 'menu'
MAIN_MENU_EP = '/MainMenu'
MAIN_MENU_NM = "Welcome to Text Game!"
HELLO_EP = '/hello'
HELLO_RESP = 'hello'
GAMES_EP = '/games'
DEL_GAME_EP = f'{GAMES_EP}/{DELETE}'
GAME_MENU_EP = '/game_menu'
GAME_MENU_NM = 'Game Menu'
GAME_ID = 'Game ID'
USERS_EP = '/users'
USER_MENU_EP = '/user_menu'
USER_MENU_NM = 'User Menu'
TYPE = 'Type'
DATA = 'Data'
TITLE = 'Title'
RETURN = 'Return'


@api.route(HELLO_EP)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO_RESP: 'world'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route(f'{MAIN_MENU_EP}')
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {TITLE: MAIN_MENU_NM,
                DEFAULT: 2,
                'Choices': {
                    '1': {'url': '/', 'method': 'get',
                          'text': 'List Available Characters'},
                    '2': {'url': '/',
                          'method': 'get', 'text': 'List Active Games'},
                    '3': {'url': f'{USERS_EP}',
                          'method': 'get', 'text': 'List Users'},
                    '4': {'url': '/',
                          'method': 'get', 'text': 'Illustrating a Point!'},
                    'X': {'text': 'Exit'},
                }}


@api.route(f'{USER_MENU_EP}')
class UserMenu(Resource):
    """
    This will deliver our user menu.
    """
    def get(self):
        """
        Gets the user menu.
        """
        return {
                   TITLE: USER_MENU_NM,
                   DEFAULT: '0',
                   'Choices': {
                       '1': {
                            'url': '/',
                            'method': 'get',
                            'text': 'Get User Details',
                       },
                       '0': {
                            'text': 'Return',
                       },
                   },
               }


@api.route(f'{USERS_EP}')
class Users(Resource):
    """
    This class supports fetching a list of all users.
    """
    def get(self):
        """
        This method returns all users.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Games',
            DATA: users.get_users(),
            MENU: USER_MENU_EP,
            RETURN: MAIN_MENU_EP,
        }


@api.route(f'{DEL_GAME_EP}/<name>')
class DelGame(Resource):
    """
    Deletes a game by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, name):
        """
        Deletes a game by name.
        """
        try:
            gm.del_game(name)
            return {name: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


game_fields = api.model('NewGame', {
    gm.NAME: fields.String,
    gm.NUM_PLAYERS: fields.Integer,
})


@api.route(f'{GAMES_EP}')
class Games(Resource):
    """
    This class supports various operations on games, such as
    listing them, and adding a game.
    """
    def get(self):
        """
        This method returns all games.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Games',
            DATA: gm.get_games(),
            MENU: GAME_MENU_EP,
            RETURN: MAIN_MENU_EP,
        }

    @api.expect(game_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a game.
        """
        name = request.json[gm.NAME]
        num_players = request.json[gm.NUM_PLAYERS]
        try:
            new_id = gm.add_game(name, num_players)
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {GAME_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')


@api.route(f'{GAMES_EP}/<name>/<num_players>')
class NumPlayers(Resource):
    """
    Updates the number of players in a game.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def put(self, name, num_players):
        """
        Update the number of players in a game.
        """
        try:
            gm.update_num_players(name, num_players)
            return {name: 'Updated'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')
