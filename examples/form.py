"""
This module provides the glossary query form
"""

import examples.form_filler as ff

from examples.form_filler import FLD_NM  # for tests

ACRONYM = 'acronym'
TERM = 'term'

GLOSSARY_FORM_FLDS = [
    {
        FLD_NM: 'Instructions',
        ff.QSTN: 'Leave all fields blank to see all glossary entries.',
        ff.INSTRUCTIONS: True,
    },
    {
        FLD_NM: ACRONYM,
        ff.QSTN: 'Acronym:',
        ff.PARAM_TYPE: ff.QUERY_STR,
        ff.OPT: True,
    },
    {
        FLD_NM: TERM,
        ff.QSTN: 'Term:',
        ff.PARAM_TYPE: ff.QUERY_STR,
        ff.OPT: True,
    },
]


def get_form() -> list:
    return GLOSSARY_FORM_FLDS


def get_form_descr() -> dict:
    """
    For Swagger!
    """
    return ff.get_form_descr(GLOSSARY_FORM_FLDS)


def get_fld_names() -> list:
    return ff.get_fld_names(GLOSSARY_FORM_FLDS)


def main():
    # print(f'Form: {get_form()=}\n\n')
    print(f'Form: {get_form_descr()=}\n\n')
    # print(f'Field names: {get_fld_names()=}\n\n')


if __name__ == "__main__":
    main()
