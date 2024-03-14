"""
Tests for examples/form.py.
"""
import examples.form as fm


def test_get_form():
    form = fm.get_form()
    assert isinstance(form, list)
    assert len(form) > 0
    for fld in form:
        # Every field must have a name!
        assert fm.FLD_NM in fld
        # And it can't be blank.
        assert len(fld[fm.FLD_NM]) > 0


def test_get_form_descr():
    assert isinstance(fm.get_form_descr(), dict)


def test_get_fld_names():
    assert isinstance(fm.get_fld_names(), list)
