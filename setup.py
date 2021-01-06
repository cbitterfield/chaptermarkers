#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

__author__ = 'Colin Bitterfield'

import io
import pip

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import setup, find_packages

PACKAGE_NAME = 'chaptermarkers'
DESCRIPTION = 'chaptermarkers writes markers to MP4 files.'


def read(*filenames, **kwargs):
    """Gets file content"""
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = list()
    for filename in filenames:
        with io.open(filename, encoding=encoding) as open_file:
            buf.append(open_file.read())
    return sep.join(buf)


def get_parsed_req(req_file):
    """Gets requirement from file"""
    parsed_req = parse_requirements(req_file, session=False)
    return (str(ir.requirement) for ir in parsed_req)


REQUIREMENTS = get_parsed_req('requirements/prod.txt')
TEST_REQUIREMENTS = get_parsed_req('requirements/test.txt')
SETUP_REQUIREMENTS = ['pytest-runner==4.2']


setup(
    name=PACKAGE_NAME,
    version='1.0.0',
    author='Colin Bitterfield',
    author_email='cbitterfield@gmail.com',
    description=DESCRIPTION,
    long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    keywords='',
    packages=find_packages(include=[PACKAGE_NAME], exclude='tests'),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    include_package_data=True,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    url='https://github.com/cbitterfield/chaptermarkers.git',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'chaptermarkers=chaptermarkers.chaptermarkers:main',
        ],
    },
    license="MIT license",
)
