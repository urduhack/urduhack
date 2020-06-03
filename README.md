Urduhack: A Python NLP library for Urdu language
=================================================

[![image](https://img.shields.io/pypi/pyversions/urduhack.svg)](https://pypi.org/project/urduhack/)
[![image](https://img.shields.io/pypi/v/urduhack.svg)](https://pypi.org/project/urduhack/)
[![Azure DevOps builds](https://img.shields.io/azure-devops/build/urduhack/urduhack/1?logo=azure-pipelines)](https://dev.azure.com/Urduhack/Urduhack/_build?definitionId=1)
[![Azure DevOps tests](https://img.shields.io/azure-devops/tests/urduhack/urduhack/1?logo=azure-pipelines)](https://dev.azure.com/Urduhack/Urduhack/_build?definitionId=1)
[![Build Status](https://img.shields.io/travis/urduhack/urduhack?label=linux%20build&logo=travis)](https://travis-ci.org/urduhack/urduhack)
[![CodeFactor](https://www.codefactor.io/repository/github/urduhack/urduhack/badge)](https://www.codefactor.io/repository/github/urduhack/urduhack)
[![codecov](https://codecov.io/gh/urduhack/urduhack/branch/master/graph/badge.svg)](https://codecov.io/gh/urduhack/urduhack)
[![image](https://img.shields.io/github/contributors/urduhack/urduhack.svg)](https://github.com/urduhack/urduhack/graphs/contributors)
[![Downloads](https://pepy.tech/badge/urduhack)](https://pepy.tech/project/urduhack)
[![Gitter](https://badges.gitter.im/urduhack/urduhack.svg)](https://gitter.im/urduhack/urduhack?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/urduhack/urduhack/blob/master/LICENSE)


Urduhack is a NLP library for urdu language. It comes with a lot of battery included features to help you process Urdu
data in the easiest way possible.


🔥 Features Support
----------------
- [x] Normalization
    - [x] Arabic and Urdu Unicode Redundancy Problem
    - [x] Character Normalization
    - [x] Combined Characters Normalization 
    - [x] Diacritics Removal
    - [x] Spaces Before & After Digits
    - [x] Spaces After Punctuations
    - [x] Joined Words Fix
- [x] Tokenization
    - [x] Sentence Tokenization
    - [x] Words Tokenization
 - [x] Data Pre-processing
     - [x] Handles all kind of numbers, emails, currencies and urls etc.
- [ ] Tasks
  - [x] Sentimental analysis
  - [ ] Sentence classification
  - [ ] Documents classification
  - [ ] Name entity recognition
  - [ ] Image to text
  - [ ] Speech to text
- [x] Datasets
  - [x] IMDB Urdu movies review dataset
  - [x] Hand written digits datasets


🛠 Installation
------------
Urduhack officially supports Python 3.6–3.7, and runs great on PyPy.

Installing with tensorflow cpu version.
``` {.sourceCode .bash}
$ pip install urduhack[tf]
```

Installing with tensorflow gpu version.
``` {.sourceCode .bash}
$ pip install urduhack[tf-gpu]
```

🔗 Documentation
-------------
Fantastic documentation is available at <https://urduhack.readthedocs.io/>

| Documentation   |                                                                |
| --------------- | -------------------------------------------------------------- |
| [Installation]  | How to install Urduhack and download models                    |
| [Quickstart]    | New to Urduhack? Here's everything you need to know!           |
| [API Reference] | The detailed reference for Urduhack's API.                     |

[Installation]: https://urduhack.readthedocs.io/en/stable/installation.html
[Quickstart]: https://urduhack.readthedocs.io/en/stable/quickstart/index.html
[Api reference]: https://urduhack.readthedocs.io/en/stable/reference/index.html



How to Contribute
-----------------
1.  Check for open issues or open a fresh issue to start a discussion
    around a feature idea or a bug. There is a [Contributor Friendly](https://github.com/urduhack/urduhack/issues)
    tag for issues that should be ideal for people who are not very
    familiar with the codebase yet.
3.  Write a test which shows that the bug was fixed or that the feature
    works as expected.
4.  Send a pull request and bug the maintainer until it gets merged and
    published. :)

👍 Contributors
-------------
Special thanks to everyone who contributed to getting the UrduHack to the current state.

Backers [![Backers on Open Collective](https://opencollective.com/urduhack/backers/badge.svg)](#backers)
---------------------------------------------------------------------------------------------------------
Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/urduhack#backer)]
<a href="https://opencollective.com/urduhack#backers" target="_blank"><img src="https://opencollective.com/urduhack/backers.svg?width=890"></a>

Sponsors [![Sponsors on Open Collective](https://opencollective.com/urduhack/sponsors/badge.svg)](#sponsors)
-----------------------------------------------------------------------------------------------------------------
Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/urduhack#sponsor)]
<a href="https://opencollective.com/urduhack/sponsor/0/website" target="_blank"><img src="https://opencollective.com/urduhack/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/urduhack/sponsor/1/website" target="_blank"><img src="https://opencollective.com/urduhack/sponsor/1/avatar.svg"></a>

📝 Copyright and license
---------------------
Code released under the [MIT License](ttps://github.com/urduhack/urduhack/blob/master/LICENSE).