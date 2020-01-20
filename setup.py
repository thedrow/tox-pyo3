#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='tox-pyo3',
    description='Build a rust extension using PyO3 using tox.',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    version='1.0.0',
    author='Omer Katz',
    author_email='omer.drow@gmail.com',
    maintainer='Omer Katz',
    maintainer_email='omer.drow@gmail.com',
    url='https://github.com/thedrow/tox-pyo3',
    packages=find_packages(),
    python_requires='>=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*,!=3.4.*',
    install_requires=['tox>=3.0.0', "pathlib2;python_version<='3.5'"],
    entry_points={'tox': ['pyo3 = tox_pyo3.plugin']},
    license='BSD-3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: tox',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
)
