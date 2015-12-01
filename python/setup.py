#!/usr/bin/env python
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

long_description = open('../README').read()
license = open('../COPYRIGHT').read()

setup(
    name='libsvm',
    version="1.0",
    packages=find_packages(),
    long_description=long_description,
    author="Lloyd Zhou",
    author_email="lloydzhou@qq.com",
    description="This is an libsvm Package",
    license=license,
    keywords="libsvm",
    url="https://github.com/lloydzhou/libsvm",   # project home page, if any

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)


