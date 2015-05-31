#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_twitter

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_twitter.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='djangocms-twitter2',
    version=version,
    description="""The easiest way to display tweets for your django-cms powered site, using the latest Twitter 1.1 API. It's a great option for embedding tweets on your site without third-party widgets.""",
    long_description=readme,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/djangocms-twitter2',
    packages=[
        'djangocms_twitter',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'django-connected',
        'django-cms>=3.0',
        'requests',
        'tweepy',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-twitter2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
