
"""
This module manages person roles for a journal.
"""
AUTHOR_CODE = 'AU'
TEST_CODE = AUTHOR_CODE

ROLES = {
    AUTHOR_CODE: 'Author',
    'ED': 'Editor',
    'RE': 'Referee',
}


def get_roles() -> dict:
    return ROLES


def is_valid(code: str) -> bool:
    return code in ROLES


def main():
    print(get_roles())


if __name__ == '__main__':
    main()
