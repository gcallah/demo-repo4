import pytest

import data.db_connect as dbc

TEST_DB = dbc.GAME_DB
TEST_COLLECT = 'test_collect'
# can be used for field and value:
TEST_NAME = 'test'
UPDATE = 'Update'


@pytest.fixture(scope='function')
def temp_rec():
    dbc.connect_db()
    dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
    # yield to our test function
    yield
    dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})


def test_fetch_one(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: TEST_NAME})
    assert ret is not None


def test_fetch_one_not_there(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: 'not a field value in db!'})
    assert ret is None


def test_update_doc(temp_rec):
    dbc.update_doc(TEST_COLLECT, {TEST_NAME: TEST_NAME}, {TEST_NAME: UPDATE})
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: UPDATE})
    assert ret is not None
