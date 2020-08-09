# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys
import os

WD = '/'.join(sys.argv[0].split('/')[:-1])
if WD > '':
    os.chdir(WD)

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('pyusng/__init__.py', 'rt') as v:
    for row in v:
        version = None
        if row.startswith('__version__ = '):
            version = row[14:].strip().strip('"')
            break
    assert version is not None
    with open('version.txt', 'wt') as f:
        f.write(version)

setup(
    name='pyusng',
    version=version,
    description='Pure PYthon tool to compute USNG coordinates from Latitude/Longitude',
    long_description=readme,
    author='Carl Anderson',
    author_email='carl.anderson@nltgis.com',
    url='https://github.com/NLTGit/usng-py.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
    ],
    entry_points={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL License",
        "Operating System :: OS Independent",
    ]

)
