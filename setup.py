#!/usr/bin/env python

import re
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-exabackend',
    long_description="EXASOL DB backend for Django",
    version="0.0.5",
    license="N/A",
    maintainer="Oleksandr Kozachuk",
    maintainer_email="oleksandr.kozachuk@exasol.com",
    description="EXASOL DB backend for Django.",
#    url='https://github.com/aurorasoftware/django-pyodbc',
    url='://github.com/EXASOL/django-exasol',
    package_data={'': ['README.md']},
    packages=[
        'django_exabackend',
    ],
    install_requires=[
        'pyodbc>=3.0.6,<3.1',
    ]
)
