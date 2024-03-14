
"""
A utility for filling in a form in a notebook or
from the command line.
"""
FLD_NM = 'fld_nm'
QSTN = 'question'
DESCR = 'description'
INSTRUCTIONS = 'instructions'
OPT = 'optional'
CHOICES = 'choices'
SUBFIELDS = 'subfields'
MULTI = 'multiple'  # choice field that allows > 1 choice
RANGE = 'range'  # designates a field that selects a range of values
DEFAULT = 'default'
TYPECAST = 'typecast'
LOW_VAL = 'low_val'
MID_VAL = 'mid_val'
HI_VAL = 'hi_val'
INT = 'int'
BOOL = 'bool'
LIST = 'list'
MARKDOWN = 'markdown'
REQ_LEN = 'req_len'
INPUT_TYPE = 'input_type'
RECOMMENDED_PAGE = 'recommended_page'
URL = 'url'
PARAM_TYPE = 'param_type'
# two parameter types:
PATH = 'path'
QUERY_STR = 'query_string'
# some input types:
FILE_LOADER = 'file_loader'
DATE = 'date'
PASSWORD = 'password'
NUMERIC = 'numeric'  # a string, but only numbers allowed
# for strings, we might want non-default input box sizes:
FLD_LEN = 'fld_len'
PARAMS = 'params'
# sometimes we don't want 'None' as the default in a pick list:
ALL = 'All'
NONE = 'None'

DISP_NAME = 'name'
DESCR = 'description'
LOW_VAL = 'low_value'
HI_VAL = 'high_value'

TEST_FLD = 'test field'

TEST_FLD_DESCRIPS = [
    {
        FLD_NM: TEST_FLD,
        DEFAULT: 'test default',
        PARAM_TYPE: QUERY_STR,
        QSTN: 'Why do we never get an answer?',
    }
]


BOOL_CHOICES = {
    True: 'Yes',
    False: 'No',
}


def get_form_descr(fld_descrips: list) -> dict:
    descr = {}
    for fld in fld_descrips:
        if fld.get(PARAM_TYPE, '') == QUERY_STR:
            fld_nm = fld[FLD_NM]
            descr[fld_nm] = fld[QSTN]
            if CHOICES in fld:
                descr[fld_nm] += f'\nChoices: {fld[CHOICES]}'
    return descr


def get_fld_names(fld_descrips: list) -> list:
    fld_nms = []
    for fld in fld_descrips:
        fld_nms.append(fld[FLD_NM])  # every field MUST have a name!
    return fld_nms


def get_query_fld_names(fld_descrips: list) -> list:
    fld_nms = []
    for fld in fld_descrips:
        if fld[PARAM_TYPE] == QUERY_STR:
            fld_nms.append(fld[FLD_NM])  # every field MUST have a name!
    return fld_nms


def get_input(dflt, opt, qstn):
    """
    So we can mock patch this.
    """
    return input(f'{dflt}{opt}{qstn} ')


def form(fld_descrips):
    print('For optional fields just hit Enter if you do not want a value.')
    print('For fields with a default just hit Enter if you want the default.')
    fld_vals = {}
    for fld in fld_descrips:
        opt = ''
        dflt = ''
        if CHOICES in fld:
            print(f'Options: {fld[CHOICES]}')
        if OPT in fld:
            opt = '(OPTIONAL) '
        if DEFAULT in fld:
            dflt = f'(DEFAULT: {fld["default"]}) '
        # no question means don't ask the user:
        if QSTN in fld:
            fld_vals[fld[FLD_NM]] = get_input(dflt, opt, fld[QSTN])
            if TYPECAST in fld:
                if fld[TYPECAST] == INT:
                    fld_vals[fld[FLD_NM]] = int(fld_vals[fld[FLD_NM]])
        else:
            fld_vals[fld[FLD_NM]] = ''
        # See if we should fill in default val:
        if DEFAULT in fld and not fld_vals[fld[FLD_NM]]:
            fld_vals[fld[FLD_NM]] = fld["default"]
    return fld_vals


def main():
    result = form(TEST_FLD_DESCRIPS)
    print(result)


if __name__ == "__main__":
    main()
