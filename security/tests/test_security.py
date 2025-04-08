import pytest

import security.security as sec


def test_check_login_good():
    assert sec.check_login(sec.GOOD_USER_ID,
                           login_key='any key will do for now')


def test_check_login_bad():
    assert not sec.check_login(sec.GOOD_USER_ID)


def test_read():
    recs = sec.read()
    assert isinstance(recs, dict)
    for feature in recs:
        assert isinstance(feature, str)
        assert len(feature) > 0


def test_read_feature():
    feature = sec.read_feature(sec.PEOPLE)
    assert isinstance(feature, dict)


def test_is_permitted_no_such_feature():
    assert sec.is_permitted('Non-existent feature', sec.CREATE, 'any user')


def test_is_permitted_action_missing():
    assert sec.is_permitted(sec.PEOPLE, sec.PEOPLE_MISSING_ACTION, 'any user')


def test_is_permitted_bad_user():
    assert not sec.is_permitted(sec.PEOPLE, sec.CREATE, 'non-existent user')


def test_is_permitted_bad_check():
    with pytest.raises(ValueError):
        sec.is_permitted(sec.BAD_FEATURE, sec.CREATE, sec.GOOD_USER_ID)


def test_is_permitted_all_good():
    assert sec.is_permitted(sec.PEOPLE, sec.CREATE, sec.GOOD_USER_ID,
                            login_key='any key for now')
