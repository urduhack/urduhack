# coding: utf8
"""Project Meta data description"""
import platform
from pathlib import Path
from typing import Dict

__version__ = '1.1.1'
__description__ = 'Natural Language Processing (NLP) library for Urdu language.'
__url__ = 'https://github.com/urduhack/urduhack'
__author__ = 'Ikram Ali'
__author_email__ = 'mrikram1989@gmail.com'
__license__ = 'MIT License'


def get_info() -> Dict[str, str]:
    """
    Get system info about Urduhack library.
    prints details in Markdown for easy copy-pasting to GitHub issues.

    Returns:
        dict: Urduhack library info
    """
    return {
        "urduhack_version": __version__,
        "location": str(Path(__file__).parent.parent),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
    }
