# coding=utf-8
""""Errors module"""


def add_codes(cls):
    """Add error messages with Code for easy debugging"""

    class ErrorsWithCodes:  # pylint: disable=too-few-public-methods
        """Add error messages with Code for easy debugging
        """

        def __getattribute__(self, code):
            msg = getattr(cls, code)
            return f'[{code}] {msg}'

    return ErrorsWithCodes()


@add_codes
class Errors:  # pylint: disable=too-few-public-methods
    """Error messages with code"""
    E000 = "{message}"
    E001 = "{object_name} must be {object_type} type."
    E002 = "{object_name} does not exist."
