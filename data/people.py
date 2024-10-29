"""
This module interfaces to our user data.
"""
import re

import data.roles as rls

MIN_USER_NAME_LEN = 2
# fields
NAME = 'name'
ROLES = 'roles'
AFFILIATION = 'affiliation'
EMAIL = 'email'

TEST_EMAIL = 'ejc369@nyu.edu'
DEL_EMAIL = 'delete@nyu.edu'

people_dict = {
    TEST_EMAIL: {
        NAME: 'Eugene Callahan',
        ROLES: [],
        AFFILIATION: 'NYU',
        EMAIL: TEST_EMAIL,
    },
    DEL_EMAIL: {
        NAME: 'Another Person',
        ROLES: [],
        AFFILIATION: 'NYU',
        EMAIL: DEL_EMAIL,
    },
}


CHAR_OR_DIGIT = '[A-Za-z0-9]'
VALID_CHARS = '[A-Za-z0-9_.]'


def is_valid_email(email: str) -> bool:
    return re.fullmatch(f"{VALID_CHARS}+@{CHAR_OR_DIGIT}+"
                        + "\\."
                        + f"{CHAR_OR_DIGIT}"
                        + "{2,3}", email)


def read() -> dict:
    """
    Our contract:
        - No arguments.
        - Returns a dictionary of users keyed on user email.
        - Each user email must be the key for another dictionary.
    """
    people = people_dict
    return people


def read_one(email: str) -> dict:
    """
    Return a person record if email present in DB,
    else None.
    """
    return people_dict.get(email)


def delete(_id):
    people = read()
    if _id in people:
        del people[_id]
        return _id
    else:
        return None


def is_valid_person(name: str, affiliation: str, email: str,
                    role: str = None, roles: list = None) -> bool:
    if not is_valid_email(email):
        raise ValueError(f'Invalid email: {email}')
    if role:
        if not rls.is_valid(role):
            raise ValueError(f'Invalid role: {role}')
    elif roles:
        for role in roles:
            if not rls.is_valid(role):
                raise ValueError(f'Invalid role: {role}')
    return True


def create(name: str, affiliation: str, email: str, role: str):
    if email in people_dict:
        raise ValueError(f'Adding duplicate {email=}')
    if is_valid_person(name, affiliation, email, role=role):
        roles = []
        if role:
            roles.append(role)
        people_dict[email] = {NAME: name, AFFILIATION: affiliation,
                              EMAIL: email, ROLES: roles}
        return email


def update(name: str, affiliation: str, email: str, roles: list):
    if email not in people_dict:
        raise ValueError(f'Updating non-existent person: {email=}')
    if is_valid_person(name, affiliation, email, roles=roles):
        people_dict[email] = {NAME: name, AFFILIATION: affiliation,
                              EMAIL: email, ROLES: roles}
        return email


def get_masthead() -> dict:
    masthead = {}
    mh_roles = rls.get_masthead_roles()
    for mh_role, text in mh_roles.items():
        people_w_role = {}
        for person in read():
            pass
            # if has_role(person):
            #     put their record in people_w_role
        masthead[text] = people_w_role
    return masthead


def main():
    print(get_masthead())


if __name__ == '__main__':
    main()
