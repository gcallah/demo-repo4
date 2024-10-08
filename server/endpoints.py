"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
# from http import HTTPStatus

from flask import Flask  # , request
from flask_restx import Resource, Api  # Namespace, fields
from flask_cors import CORS

# import werkzeug.exceptions as wz

import data.people as ppl

app = Flask(__name__)
CORS(app)
api = Api(app)

DATE = '2024-09-24'
DATE_RESP = 'Date'
EDITOR = 'ejc369@nyu.edu'
EDITOR_RESP = 'Editor'
ENDPOINT_EP = '/endpoints'
ENDPOINT_RESP = 'Available endpoints'
HELLO_EP = '/hello'
HELLO_RESP = 'hello'
PEOPLE_EP = '/people'
PUBLISHER = 'Palgave'
PUBLISHER_RESP = 'Publisher'
TITLE = 'The Journal of API Technology'
TITLE_EP = '/title'
TITLE_RESP = 'Title'


@api.route(HELLO_EP)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        """
        return {HELLO_RESP: 'world'}


@api.route(ENDPOINT_EP)
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a sorted list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route(TITLE_EP)
class JournalTitle(Resource):
    """
    This class handles creating, reading, updating
    and deleting the journal title.
    """
    def get(self):
        """
        Retrieve the journal title.
        """
        return {
            TITLE_RESP: TITLE,
            EDITOR_RESP: EDITOR,
            DATE_RESP: DATE,
            PUBLISHER_RESP: PUBLISHER,
        }


@api.route(PEOPLE_EP)
class People(Resource):
    """
    This class handles creating, reading, updating
    and deleting journal people.
    """
    def get(self):
        """
        Retrieve the journal people.
        """
        return ppl.get_people()


@api.route(f'{PEOPLE_EP}/<_id>')
class PersonDelete(Resource):
    def delete(self, _id):
        ret = ppl.delete_person(_id)
        return {'Message': ret}


# PEOPLE_CREATE_FLDS = api.model('AddNewPeopleEntry', {
#     pflds.NAME: fields.String,
#     pflds.EMAIL: fields.String,
#     pflds.AFFILIATION: fields.String,
#     EDITOR: fields.String,
# })


# PEOPLE_CREATE_FORM = 'People Add Form'


# @api.route(f'/{PEOPLE}/{CREATE}/{FORM}')
# class PeopleAddForm(Resource):
#     """
#     Form to add a new person to the journal database.
#     """
#     def get(self):
#         return {PEOPLE_CREATE_FORM: pfrm.get_add_form()}


# @api.route(f'/{PEOPLE}/{CREATE}')
# @api.expect(parser)
# class PeopleCreate(Resource):
#     """
#     Add a person to the journal db.
#     """
#     @api.response(HTTPStatus.OK, 'Success')
#     @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not acceptable')
#     @api.expect(PEOPLE_CREATE_FLDS)
#     def put(self):
#         """
#         Add a person.
#         """
#         user_id, auth_key = _get_user_info(request)
#         if not sm.is_permitted(PROTOCOL_NM, sm.CREATE, user_id=user_id,
#                                auth_key=auth_key):
#             raise wz.Forbidden('Action not permitted.')
#         try:
#             ret = pqry.add(request.json)
#         except Exception as err:
#             raise wz.NotAcceptable(f'Could not add person: '
#                                    f'{err=}')
#         return {
#             MESSAGE: 'Person added!', 'ret': ret,
#         }
