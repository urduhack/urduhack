# CONTRIBUTE TO URUHACK

Guide on how you can contribute to urduhack

## Vision

Our vision is to provide state of the art Machine Learning models in Urduhack for urdu language.

## CONTRIBUTION GUIDE

1. [Issues and Bugs](#issues-and-bugs)
2. [Code Contribution](#code-contribution)
3. [Add or Improve a Machine Learning Models](#add-or-improve-machine-learning-models)
4. [Code Conventions](#code-convention)
5. [Add Test Cases](#add-test-cases)
6. [Code of Conduct](#code-of-conduct)

## Issues and Bugs

If you have encountered an issue, quickly [search](https://github.com/urduhack/urduhack/issues) to see
if this issue has already been raised. Remember! it is always better to look in the old issue as
if often contains helpful tips and solutions.

If you there as a problem in your code and you are seeking help from [Stack Overflow](https://stackoverflow.com/questions/tagged/urduhack),
do tag `urduhack` and `python` as more people will be able to see it and help.

### Submitting an Issue
If you want to open a new issue, follow our [template](https://github.com/urduhack/urduhack/issues/new?template=01_bugs.md).
Always use a **descriptive title** for the issue and mention your **environment** (Operating system, Python version, Urduhack version) details.
Some other tips for submitting an issue:

-   **Describing your issue:** Try to provide as many details as possible. What
    exactly goes wrong? _How_ is it failing? Is there an error?
    "XY doesn't work" usually isn't that helpful for tracking down problems. Always
    remember to include the code you ran and if possible, extract only the relevant
    parts and don't just dump your entire script. This will make it easier for us to
    reproduce the error.

-   **Getting info about your Urduhack installation and environment:** To get information about urduhack
    version and system, you can use `urduhack.get_info()` method.

-   **Sharing long blocks of code or logs:** If you need to include long code,
    logs or tracebacks, you can wrap them in `<details>` and `</details>`. This
    [collapses the content](https://developer.mozilla.org/en/docs/Web/HTML/Element/details)
    so it only becomes visible on click, making the issue easier to read and follow.
    
### Issues labels
To check the labels we use for our issue, [click here](https://github.com/urduhack/urduhack/labels).

## Code Contribution
If you are a developer and want to add some functionality to urduhack or you think a part of the existing code needs
modifications, follow the steps

-   Clone the urduhack github repo via `git clone https://github.com/urduhack/urduhack.git` or you can clone
    it in Pycharm or any other IDE.
-   Create a branch and remember your branch name must reflect the purpose.
-   Make the changes
-   Write the test cases
-   Run it locally by installing using `pip install -e .` to check if the changes are working
-   Test if the test case is passed with `pytest`
-   Push the changes to urduhack and create a pull request from your branch.

## Add or Improve Machine Learning Models

We have open sourced Urduhack models code. Either you've got your own dataset or you can request for the dataset. Train
the models, optimize the parameters and if you get any improvements in the models , you can create a pull request for the
update of the model.

Procedure will be added soon!!

## Code Convention
Code should loosely follow [PEP8](https://www.python.org/dev/peps/pep-0008/) conventions. Use `pylint` for linting python
modules and use `google-docs` for module documentation.

To know more about PEP8 conventions, read the [docs](https://www.python.org/dev/peps/pep-0008/).

## Add Test Cases
Urduhack uses `pytest` for testing. Test cases for each module reside in a directory named tests in the same module.
To know more about pytest, read the pytest [documentation](http://docs.pytest.org/en/latest/contents.html)

When adding test cases, use the same name of the function with the prefix `test_`. Code should be short and concise for test
case and only test one behaviour at a time.
