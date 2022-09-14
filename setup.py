# Prepare a release:
#
#  - fill the changelog
#  - run unit tests on Linux: run "tox"
#  - run unit tests on Windows, run::
#
#       \Python27\python.exe runtest.py -r
#       \Python27\python.exe runtest.py -r -m
#
#  - update the version in setup.py and doc/conf.py to X.Y
#  - check that "python setup.py sdist" contains all files tracked by
#    the SCM (Mercurial): update MANIFEST.in if needed
#  - set release date in doc/changelog.rst
#  - hg ci
#  - hg push
#
# Release a new version:
#
#  - hg tag X.Y
#  - hg push
#  - python setup.py sdist register upload
#    WARNING: don't publish binary wheel packages, since setup.py
#             hardcodes dependencies depending on the Python version.
#  - increment version in setup.py and doc/conf.py
#  - hg ci && hg push
#
# After the release:
#
#  - increment version in setup.py and doc/conf.py
#  - hg ci -m "post-release" && hg push

import sys
try:
    from setuptools import setup
    SETUPTOOLS = True
except ImportError:
    SETUPTOOLS = False
    # Use distutils.core as a fallback.
    # We won't be able to build the Wheel file on Windows.
    from distutils.core import setup

requirements = ['eventlet']
if sys.version_info >= (3, 4):
    # Python 3.4 and newer: asyncio is now part of the stdlib
    pass
elif (3, 3) <= sys.version_info < (3, 4):
    # Python 3.3: use Tulip
    requirements.append('asyncio>=0.4.1')
else:
    # Python 2.7: use Trollius
    requirements.append('trollius>=0.3')

with open("README") as fp:
    long_description = fp.read()

install_options = {
    "name": "faust-aioeventlet",
    "version": "0.6",
    "license": "Apache License 2.0",
    "author": 'Victor Stinner',
    "author_email": 'victor.stinner@gmail.com',

    "description": "asyncio event loop scheduling callbacks in eventlet.",
    "long_description": long_description,
    "url": "http://aioeventlet.readthedocs.org/",

    "classifiers": [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],

    "py_modules": ["aioeventlet"],
    #"test_suite": "runtests.runtests",
}
if SETUPTOOLS:
    install_options['install_requires'] = requirements

setup(**install_options)
