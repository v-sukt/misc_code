#!/usr/bin/python python

try:
    from setuptools import setup
except:
    from distutils.core import setup


config = {
    'description': 'Example 48 project',
    'author': 'v-sukt',
    'url': 'URL to get it at',
    'download_url': 'Where to Download it.',
    'author_mail': 'v-sukt@users.noreply.github.com',
    'version': '0.1',
    'install_requires': ['nose>=0'], # the Packages required by this package
    'packages': ['ex48_project'], # The packages from . or $PWD to be installed
    'scripts': ['bin/dummy'],   #the scripts that need to be installed
    'name': 'ex48_project_pkg'
}

setup(**config)
