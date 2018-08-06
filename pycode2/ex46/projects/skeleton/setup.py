#!/usr/bin/python python

try:
    from setuptools import setup
except:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at',
    'download_url': 'Where to Download it.',
    'author_mail': 'My_email@mail.ext',
    'version': '0.1',
    'install_requires': ['nose>=0'], # the Packages required by this package
    'packages': ['NAME'], # The packages from . or $PWD to be installed
    'scripts': ['bin/dummy'],   #the scripts that need to be installed
    'name': 'projectname'
}

setup(**config)
