#!/usr/bin/env python

from setuptools import setup
import bashpunchcard

setup(
    name             = 'bashpunchcard',
    version          = bashpunchcard.__version__,
    description      = bashpunchcard.__description__,

    author           = bashpunchcard.__author__,
    author_email     = 'askedrelic@gmail.com',
    url              = 'https://github.com/askedrelic/bash-history-punchcard',
    license          = open("LICENSE.txt").read(),

    packages         = ['bashpunchcard'],
    install_requires = ['pygooglechart >= 0.3.0'],
    zip_safe         = True,
    entry_points = {
        'console_scripts': [
            'bashpunchcard = bashpunchcard:main',
        ],
    },

    classifiers      = (
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
        'Environment :: Console'
    ),
)
