# coding=utf-8
""""Errors module"""


def add_codes(cls):
    """Add error messages with Code for easy debugging"""

    class ErrorsWithCodes(object):
        """Add error messages with Code for easy debugging
        """

        def __getattribute__(self, code):
            msg = getattr(cls, code)
            return f'[{code}] {msg}'

    return ErrorsWithCodes()


@add_codes
class Errors(object):
    """Error messages with code"""
    E000 = "{message}"
    E001 = "{object_name} must be {object_type} type."
