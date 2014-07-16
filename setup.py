#!/usr/bin/env python
from setuptools import setup

import os.path as op
CURRENT_DIR = op.dirname(__file__)

version = open(op.join(CURRENT_DIR, 'VERSION.txt')).read()

requirements = open(op.join(CURRENT_DIR, 'requirements.txt')).read()

setup(
    name='log_watcher',
    packages=['log_watcher'],

    author='Thomas Kliszowski',
    author_email='contact@thomaskliszowski.fr',
    description='Watch and track logs',
    license='MIT',
    keywords='watch track log',
    url='https://github.com/ThomasKliszowski/log_watcher',

    version=version,
    include_package_data=True,
    zip_safe=False,
    install_requires=[line for line in requirements.splitlines() if line and not line.startswith("--")],
    entry_points='''
        [console_scripts]
        log_watcher=log_watcher.cli:main
    ''',
)
