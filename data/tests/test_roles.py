
import data.roles as rls


def test_get_roles():
    roles = rls.get_roles()
    assert isinstance(roles, dict)
    assert len(roles) > 0
    for code, role in roles.items():
        assert isinstance(code, str)
        assert isinstance(role, str)


def test_is_valid():
    assert rls.is_valid(rls.TEST_CODE)
