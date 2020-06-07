# coding: utf8
"""Urduhack setup file"""
from pathlib import Path

from setuptools import setup, find_packages


def setup_package():
    """Packages setup functions with all required parameters"""

    package_name = 'urduhack'
    root = Path(__file__).parent.resolve()

    # Read in package meta from about.py
    about_path = root / package_name / 'about.py'
    with about_path.open('r', encoding='utf8') as file_content:
        about = {}
        exec(file_content.read(), about)

    # Get readme
    readme_path = root / 'README.md'
    with readme_path.open('r', encoding='utf8') as file_content:
        readme = file_content.read()

    # Required packages
    requirements_path = root / 'requirements.txt'
    with requirements_path.open('r', encoding='utf8') as file_content:
        requires = [line.strip('\n') for line in file_content if line.strip('\n') and not line.startswith('#')]

    setup(name=package_name,

          version=about['__version__'],

          description=about['__description__'],

          long_description=readme,

          long_description_content_type="text/markdown",

          author=about['__author__'],

          author_email=about['__author_email__'],

          url=about['__url__'],

          license=about['__license__'],

          packages=find_packages(),

          install_requires=requires,

          extras_require={
              "tf": ["tensorflow~=2.2"],
              "tf-gpu": ["tensorflow-gpu~=2.2"]
          },

          setup_requires=[],

          tests_require=[],

          zip_safe=False,

          keywords="urdu machine learning text pre-processing tensorflow nlp",

          python_requires='>= 3.6',

          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'Intended Audience :: Education',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Operating System :: POSIX :: Linux',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: Microsoft :: Windows',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'Topic :: Software Development :: Libraries',
              'Topic :: Software Development :: Libraries :: Python Modules',
              "Natural Language :: Urdu",
              "Topic :: Text Processing :: Linguistic",
          ],

          project_urls={
              "Documentation": "https://urduhack.readthedocs.io/en/stable/",
              "Source": "https://github.com/urduhack/urduhack",
              "Bug Tracker": "https://github.com/urduhack/urduhack/issues"},

          entry_points="""
            [console_scripts]
            urduhack=urduhack.command.cli:cli
        """

          )


if __name__ == '__main__':
    setup_package()
