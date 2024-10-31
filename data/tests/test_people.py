import pytest

import data.people as ppl

from data.roles import TEST_CODE as TEST_ROLE_CODE

NO_AT = 'jkajsd'
NO_NAME = '@kalsj'
NO_DOMAIN = 'kajshd@'
NO_SUB_DOMAIN = 'kajshd@com'
DOMAIN_TOO_SHORT = 'kajshd@nyu.e'
DOMAIN_TOO_LONG = 'kajshd@nyu.eedduu'

TEMP_EMAIL = 'temp_person@temp.org'


@pytest.fixture(scope='function')
def temp_person():
    _id = ppl.create('Joe Smith', 'NYU', TEMP_EMAIL, TEST_ROLE_CODE)
    yield _id
    ppl.delete(_id)


def test_create_mh_rec(temp_person):
    person_rec = ppl.read_one(temp_person)
    mh_rec = ppl.create_mh_rec(person_rec)
    assert isinstance(mh_rec, dict)
    for field in ppl.MH_FIELDS:
        assert field in mh_rec


def test_has_role(temp_person):
    person_rec = ppl.read_one(temp_person)
    assert ppl.has_role(person_rec, TEST_ROLE_CODE)


def test_doesnt_have_role(temp_person):
    person_rec = ppl.read_one(temp_person)
    assert not ppl.has_role(person_rec, 'Not a good role!')


def test_is_valid_email_no_at():
    assert not ppl.is_valid_email(NO_AT)


def test_is_valid_no_name():
    assert not ppl.is_valid_email(NO_NAME)


def test_is_valid_no_domain():
    assert not ppl.is_valid_email(NO_DOMAIN)


def test_is_valid_no_sub_domain():
    assert not ppl.is_valid_email(NO_SUB_DOMAIN)


def test_is_valid_email_domain_too_short():
    assert not ppl.is_valid_email(DOMAIN_TOO_SHORT)


def test_is_valid_email_domain_too_long():
    assert not ppl.is_valid_email(DOMAIN_TOO_LONG)


def test_is_valid_email():
    assert ppl.is_valid_email('eugene_callahan@nyu.edu')


def test_read():
    people = ppl.read()
    assert isinstance(people, dict)
    assert len(people) > 0
    # check for string IDs:
    for _id, person in people.items():
        assert isinstance(_id, str)
        assert ppl.NAME in person


def test_read_one(temp_person):
    assert ppl.read_one(temp_person) is not None


def test_read_one_not_there():
    assert ppl.read_one('Not an existing email!') is None


def test_delete():
    people = ppl.read()
    old_len = len(people)
    ppl.delete(ppl.DEL_EMAIL)
    people = ppl.read()
    assert len(people) < old_len
    assert ppl.DEL_EMAIL not in people


ADD_EMAIL = 'joe@nyu.edu'


def test_create():
    people = ppl.read()
    assert ADD_EMAIL not in people
    ppl.create('Joe Smith', 'NYU', ADD_EMAIL, TEST_ROLE_CODE)
    people = ppl.read()
    assert ADD_EMAIL in people


def test_create_duplicate():
    with pytest.raises(ValueError):
        ppl.create('Do not care about name',
                   'Or affiliation', ppl.TEST_EMAIL, TEST_ROLE_CODE)


VALID_ROLES = ['ED', 'AU']


@pytest.mark.skip('Skipping cause not done.')
def test_update(temp_person):
    ppl.update('Buffalo Bill', 'UBuffalo', temp_person, VALID_ROLES)



def test_create_bad_email():
    with pytest.raises(ValueError):
        ppl.create('Do not care about name',
                   'Or affiliation', 'bademail', TEST_ROLE_CODE)


def test_get_masthead():
    mh = ppl.get_masthead()
    assert isinstance(mh, dict)
