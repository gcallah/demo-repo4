import random

import pytest

import data.manuscripts.query as mqry


def gen_random_not_valid_str() -> str:
    """
    That huge number is only important in being huge:
        any big number would do.
    """
    BIG_NUM = 10_000_000_000
    big_int = random.randint(0, BIG_NUM)
    big_int += BIG_NUM
    bad_str = str(big_int)


def test_is_valid_state():
    for state in mqry.get_states():
        assert mqry.is_valid_state(state)


def test_is_not_valid_state():
    # run this test "a few" times
    for i in range(10):
        assert not mqry.is_valid_state(gen_random_not_valid_str())


def test_is_valid_action():
    for action in mqry.get_actions():
        assert mqry.is_valid_action(action)


def test_is_not_valid_action():
    # run this test "a few" times
    for i in range(10):
        assert not mqry.is_valid_action(gen_random_not_valid_str())


def test_handle_action_bad_state():
    with pytest.raises(ValueError):
        mqry.handle_action(gen_random_not_valid_str(),
                           mqry.TEST_ACTION)


def test_handle_action_bad_action():
    with pytest.raises(ValueError):
        mqry.handle_action(mqry.TEST_STATE,
                           gen_random_not_valid_str())


def test_handle_action_valid_return():
    for state in mqry.get_states():
        for action in mqry.get_actions():
            new_state = mqry.handle_action(state, action)
            assert mqry.is_valid_state(new_state)
