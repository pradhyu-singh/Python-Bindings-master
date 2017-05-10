#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import unicode_literals

import re
import sys

from setuptools import setup, find_packages

RE_REQUIREMENT = re.compile(r'^\s*-r\s*(?P<filename>.*)$')

def rst(filename):
    '''
    Load rst file and sanitize it for PyPI.
    Remove unsupported github tags:
     - code-block directive
     - all badges
    '''
    content = open(filename).read()
    for regex, replacement in PYPI_RST_FILTERS:
        content = re.sub(regex, replacement, content)
    return content


long_description = '\n'.join((
    rst('README.rst'),
    rst('CHANGELOG.rst'),
    ''
))


exec(compile(open('flask_restplus/__about__.py').read(), 'flask_restplus/__about__.py', 'exec'))

tests_require = ['pytest', 'pytest-sugar', 'pytest-flask', 'pytest-mock', 'pytest-faker', 'blinker', 'tzlocal', 'mock']
install_requires = ['Flask>=0.8', 'six>=1.3.0', 'pytz', 'aniso8601>=0.82', 'jsonschema']
doc_require = ['sphinx', 'alabaster', 'sphinx_issues']
qa_require = ['pytest-cover', 'flake8']
ci_require = ['invoke>=0.13'] + qa_require + tests_require
dev_require = ['minibench', 'tox'] + ci_require + doc_require

try:
    from unittest.mock import Mock
except:
    tests_require += ['mock']

setup(
    name='flask-restplus',
    version=__version__,
    description=__description__,
    long_description=long_description,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'doc': doc_require,
        'qa': qa_require,
        'ci': ci_require,
        'dev': dev_require,
    },
    license='MIT',
    use_2to3=True,
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
