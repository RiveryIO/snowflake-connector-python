#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2019 Snowflake Computing Inc. All right reserved.
#
import os
import sys
import warnings
from codecs import open
from shutil import copy
from sys import platform

from setuptools import Extension, setup

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = os.path.join(THIS_DIR, 'src')
CONNECTOR_SRC_DIR = os.path.join(SRC_DIR, 'snowflake', 'connector')

VERSION = (1, 1, 1, None)  # Default
try:
    with open(os.path.join(CONNECTOR_SRC_DIR, 'generated_version.py'), encoding='utf-8') as f:
        exec(f.read())
except Exception:
    with open(os.path.join(CONNECTOR_SRC_DIR, 'version.py'), encoding='utf-8') as f:
        exec(f.read())
version = '.'.join([str(v) for v in VERSION if v is not None])

with open(os.path.join(THIS_DIR, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()


# Parse command line flags
options = {k: 'OFF' for k in ['--opt', '--debug']}
for flag in options.keys():
    if flag in sys.argv:
        options[flag] = 'ON'
        sys.argv.remove(flag)

extensions = None
cmd_class = {}

setup(
    name='snowflake-connector-python',
    version=version,
    description="Snowflake Connector for Python",
    ext_modules=extensions,
    cmdclass=cmd_class,
    long_description=long_description,
    author='Snowflake, Inc',
    author_email='support@snowflake.com',
    license='Apache License, Version 2.0',
    keywords="Snowflake db database cloud analytics warehouse",
    url='https://www.snowflake.com/',
    download_url='https://www.snowflake.com/',
    use_2to3=False,

    python_requires='>=3.5',

    install_requires=[
        'urllib3~=1.20,<1.26.0',
        'certifi~=2021.0.0',
        'pytz~=2021.0',
        'pycryptodomex~=3.2,!=3.5.0,<4.0.0',
        'pyOpenSSL~=16.2.0,<21.0.0',
        'cffi~=1.9,<1.15',
        'cryptography~=2.5.0,<3.0.0',
        'pyjwt~=2.0.0',
        'idna~=2.11',
        'oscrypto~=2.0.0',
        'asn1crypto~=0.24.0,<2.0.0',
    ],

    namespace_packages=['snowflake'],
    packages=[
        'snowflake.connector',
        'snowflake.connector.tool',
    ],
    package_dir={
        'snowflake.connector': os.path.join('src', 'snowflake', 'connector'),
        'snowflake.connector.tool': os.path.join('src', 'snowflake', 'connector', 'tool'),
    },
    package_data={
        'snowflake.connector': ['*.pem', '*.json', '*.rst', 'LICENSE.txt'],
    },

    entry_points={
        'console_scripts': [
            'snowflake-dump-ocsp-response = '
            'snowflake.connector.tool.dump_ocsp_response:main',
            'snowflake-dump-ocsp-response-cache = '
            'snowflake.connector.tool.dump_ocsp_response_cache:main',
            'snowflake-dump-certs = '
            'snowflake.connector.tool.dump_certs:main',
            'snowflake-export-certs = '
            'snowflake.connector.tool.export_certs:main',
        ],
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',
        'Environment :: Other Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: OS Independent',

        'Programming Language :: SQL',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
