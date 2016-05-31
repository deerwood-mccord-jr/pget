#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(
    name='ParallelDownload',
    version='0.01',
    description='A library to download large files in chunks.',
    author='Halil Ozercan',
    author_email='halilozercan@gmail',
    url='https://github.com/halilozercan/paralleldownload',
    entry_points={
        'console_scripts': [
            'pdownload = ParallelDownload.bin:main',
        ],
    },
    packages=find_packages(exclude=("tests", "tests.*")),
)
