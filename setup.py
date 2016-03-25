#
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = 0.01
exec(open('WWC_recsys/_version.py').read())
readme = open('README.md').read()
description = 'library for WWC interactive session'


# For tests
setup_requires = [
    'coverage',
    'flake8',
    'nose',
    'pandas',
    'numpy',
]

setup(
    name='WWC-recsys',
    version=__version__,
    description=description,
    long_description=readme,
    packages=['WWC_recsys'],
    package_dir={'WWC-recsys': 'WWC_recsys'},
    include_package_data=True,
    setup_requires=setup_requires,
    test_suite='tests',
    authors = 'Humberto Corona, ',
)