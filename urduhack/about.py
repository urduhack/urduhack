# coding: utf8
"""Project Meta data description"""
import platform
from pathlib import Path

__version__ = '1.1.0'
__description__ = 'Natural Language Processing (NLP) library for Urdu language.'
__url__ = 'https://github.com/urduhack/urduhack'
__author__ = 'Ikram Ali'
__author_email__ = 'mrikram1989@gmail.com'
__license__ = 'MIT License'


def get_info() -> dict:
    """
    Get system info about Urduhack library.
    prints details in Markdown for easy copy-pasting to GitHub issues.

    Returns:
        dict: Urduhack library info
    """
    return {
        "Urduhack version": __version__,
        "Location": str(Path(__file__).parent.parent),
        "Platform": platform.platform(),
        "Python version": platform.python_version(),
    }
