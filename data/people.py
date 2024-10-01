"""
This module interfaces to our user data.
"""

MIN_USER_NAME_LEN = 2


def get_people():
    """
    Our contract:
        - No arguments.
        - Returns a dictionary of users keyed on user email.
        - Each user email must be the key for another dictionary.
    """
    users = {'ejc369@nyu.edu': {}}
    return users
