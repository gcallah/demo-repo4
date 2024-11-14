import data.manuscripts.fields as mflds


def test_get_flds():
    assert isinstance(mflds.get_flds(), dict)
