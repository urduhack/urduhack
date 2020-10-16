# Urduhack: A Python NLP library for Urdu language

[![image](https://img.shields.io/pypi/pyversions/urduhack.svg)](https://pypi.org/project/urduhack/)
[![image](https://img.shields.io/pypi/v/urduhack.svg)](https://pypi.org/project/urduhack/)
[![Azure DevOps builds](https://img.shields.io/azure-devops/build/urduhack/urduhack/2?logo=azure-pipelines)](https://dev.azure.com/Urduhack/Urduhack/_build?definitionId=2)
[![Azure DevOps tests](https://img.shields.io/azure-devops/tests/urduhack/urduhack/2?logo=azure-pipelines)](https://dev.azure.com/Urduhack/Urduhack/_build?definitionId=2)
[![Build Status](https://img.shields.io/travis/urduhack/urduhack?label=linux%20build&logo=travis)](https://travis-ci.org/urduhack/urduhack)
[![CodeFactor](https://www.codefactor.io/repository/github/urduhack/urduhack/badge)](https://www.codefactor.io/repository/github/urduhack/urduhack)
[![codecov](https://codecov.io/gh/urduhack/urduhack/branch/master/graph/badge.svg)](https://codecov.io/gh/urduhack/urduhack)
[![image](https://img.shields.io/github/contributors/urduhack/urduhack.svg)](https://github.com/urduhack/urduhack/graphs/contributors)
[![Downloads](https://pepy.tech/badge/urduhack)](https://pepy.tech/project/urduhack)
[![Gitter](https://badges.gitter.im/urduhack/urduhack.svg)](https://gitter.im/urduhack)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/urduhack/urduhack/blob/master/LICENSE)

Urduhack is a NLP library for urdu language. It comes with a lot of battery included features to help you process Urdu
data in the easiest way possible.

You can reach out core contributor Mr Ikram Ali @ https://github.com/akkefa

Our Goal
--------

- **Academic users** Easier experimentation to prove their hypothesis without coding from scratch.
- **NLP beginners** Learn how to build an NLP project with production level code quality.
- **NLP developers** Build a production level application within minutes.

🔥 Features Support
-------------------
- [x] Normalization
- [x] Preprocessing
- [x] Tokenization
- [x] Pipeline Module
- [x] Models
  - [x] Pos tagger
  - [x] Lemmatizer
  - [x] Name entity recognition
  - [ ] Sentimental analysis
  - [ ] Image to text
  - [ ] Question answering system
- [x] Datasets loader

🛠 Installation
---------------
Urduhack officially supports Python 3.6–3.7, and runs great on PyPy.

Installing with tensorflow cpu version.
``` {.sourceCode .bash}
$ pip install urduhack[tf]
```

Installing with tensorflow gpu version.
``` {.sourceCode .bash}
$ pip install urduhack[tf-gpu]
```

Usage
-----

```python
import urduhack

# Downloading models
urduhack.download()

nlp = urduhack.Pipeline()
text = ""
doc = nlp(text)

for sentence in doc.sentences:
    print(sentence.text)
    for word in sentence.words:
        print(f"{word.text}\t{word.pos}")

    for token in sentence.tokens:
        print(f"{token.text}\t{token.ner}")
```

🔗 Documentation
----------------
Fantastic documentation is available at <https://urduhack.readthedocs.io/>

| Documentation   |                                                                |
| --------------- | -------------------------------------------------------------- |
| [Installation]  | How to install Urduhack and download models                    |
| [Quickstart]    | New to Urduhack? Here's everything you need to know!           |
| [API Reference] | The detailed reference for Urduhack's API.                     |
| [Contribute]    | How to contribute to the code base.                            |

[Installation]: https://urduhack.readthedocs.io/en/stable/installation.html
[Quickstart]: https://urduhack.readthedocs.io/en/stable/quickstart/index.html
[Api reference]: https://urduhack.readthedocs.io/en/stable/reference/index.html
[Contribute]: https://github.com/urduhack/urduhack/blob/master/CONTRIBUTING.md
    
👍  Contributors
----------------
Special thanks to everyone who contributed to getting the Urduhack to the current state.

Backers [![Backers on Open Collective](https://opencollective.com/urduhack/backers/badge.svg)](#backers)
---------------------------------------------------------------------------------------------------------
Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/urduhack#backer)]

<a href="https://opencollective.com/urduhack#backers" target="_blank"><img src="https://opencollective.com/urduhack/backers.svg"></a>

Sponsors [![Sponsors on Open Collective](https://opencollective.com/urduhack/sponsors/badge.svg)](#sponsors)
------------------------------------------------------------------------------------------------------------
Support this project by becoming a sponsor. [[Become a sponsor](https://opencollective.com/urduhack#sponsor)]

<a href="https://opencollective.com/urduhack" target="_blank"><img src="https://opencollective.com/urduhack/sponsors.svg"></a>

📝 Copyright and license
------------------------
Code released under the [MIT License](ttps://github.com/urduhack/urduhack/blob/master/LICENSE).