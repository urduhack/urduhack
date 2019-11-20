Urduhack
========

NLP library for different Urdu language tasks. **Urduhack** has different modules all of which serve a specific purpose. You can load any of them
and check out their results by giving in your inputs. urduhack has got some magic functions that can make your life easier. You just need to access a
particular module and get amazing results by giving in your data.
Normalization, Tokenization and Preprocess are the main modules of Urduhack.

**Normalization** modules fixes the problem of correct encodings for the Urdu characters as well as replace Arabic
characters with correct Urdu characters. This module brings all the characters in the specified unicode range (0600-06FF) for Urdu language.
It also fixes the problem of joining of different Urdu words. By joining we mean that when space between two Urdu words is
removed, they must not make a new word. Their rendering must not change and even after the removal of space they should look the same.

**Tokenization** module is another crucial part of the Urduhack. This module performs tokenization on sentence. It separates different sentence from each other
and converts each string into a complete **sentence taken**. Note here you must not confuse yourself with the word token. They are two
completely different things. It handles multiple spaces and the spaces before and after a sentence. For Urdu language '۔' is a standard separator. We can specify
our custom separator and make sentence tokens.

**Preprocess** module takes care of every other type of data present in the corps. It handles *Numbers*, *Phone Numbers*, *Email Address*, *URLs*
*Line Breaks* and  *Currency Symbols* etc. It replaces all these entities with specified characters. Like we replace multiple spaces with a single space and where there
is a URL we replace it with the word 'URL'.

**Urduhack** is maintained by `Ikram Ali and Contributors <https://github.com/Urduhack/Urduhack/graphs/contributors>`_.

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/urduhack/urduhack/blob/master/LICENSE
   :alt: License: MIT

.. image:: https://img.shields.io/pypi/v/urduhack.svg
   :target: https://pypi.org/project/urduhack/
   :alt: Pypi Version

.. image:: https://img.shields.io/pypi/pyversions/urduhack.svg
   :target: https://pypi.org/project/urduhack/
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/wheel/urduhack.svg
   :target: https://pypi.org/project/urduhack/
   :alt: Wheel

.. image:: https://readthedocs.org/projects/urduhack/badge/?version=latest
   :target: https://urduhack.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/urduhack/urduhack.svg?branch=master
   :target: https://travis-ci.org/urduhack/urduhack
   :alt: Travis CI build status

.. image:: https://codecov.io/gh/urduhack/urduhack/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/urduhack/urduhack
   :alt: Code coverage

.. image:: https://img.shields.io/badge/join-us%20on%20slack-gray.svg?longCache=true&logo=slack&colorB=red
   :target: https://join.slack.com/t/urduhack/shared_invite/enQtNDE5NDg4NzU2Mzg4LTk3ZDNlYzBhOWM5MGY0ZGE0ZmNmNzU2ZTViYjAwMTg3NTBmZGU4OTM0M2E0MzQ0NDI1MDIyYzVkYTVmZTkyZjg
   :alt: Join Slack Urduhack

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/akkefa
   :alt: Say Thanks!

.. toctree::
   :maxdepth: 2

   installation.rst
   handbook/index.rst
   reference/index.rst
   about.rst
   releasenotes.rst
   deprecations.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
