#!/usr/bin/env python
#
# Copyright 2012 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3 (see the file LICENSE).

import sys
import ez_setup


ez_setup.use_setuptools()

from charmtools.version import __VERSION__
from setuptools import setup, find_packages


setup(
    name='charmtools',
    version=__VERSION__,
    packages=['charmtools'],
    install_requires=['launchpadlib', 'argparse', 'cheetah', 'pyyaml',
                      'pycrypto', 'paramiko', 'bzr'],
    package_data={'charmtools': ['templates/*/*.*', 'templates/*/hooks/*']},
    maintainer='Marco Ceppi',
    description=('Tools for maintaining Juju charms'),
    license='GPL v3',
    url='https://launchpad.net/charm-tools',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'charm = charmtools:charm',
            'juju-charm = charmtools:charm',
            'juju-bundle = charmtools:bundle',
            'charm-get = charmtools.get:main',
            'charm-getall = charmtools.getall:main',
            'charm-proof = charmtools.proof:main',
            'charm-create = charmtools.create:main',
            'charm-list = charmtools.list:main',
            'charm-promulgate = charmtools.promulgate:main',
            'charm-review = charmtools.review:main',
            'charm-review-queue = charmtools.review_queue:main',
            'charm-search = charmtools.search:main',
            'charm-subscribers = charmtools.subscribers:main',
            'charm-unpromulgate = charmtools.unpromulgate:main',
            'charm-update = charmtools.update:main',
            'charm-version = charmtools.version:main',
        ],
    },
)
