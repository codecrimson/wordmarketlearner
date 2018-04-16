# -*- coding: utf-8 -*-

# Learn more: https://github.com/codecrimson/wordmarketlearner/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wordmarketlearner',
    version='0.1.0',
    description='Keyword indexer and tensorflow processing',
    long_description=readme,
    author='Mohamed Nur',
    author_email='mohamed.nur@codecrimson.com',
    url='https://github.com/codecrimson/wordmarketlearner',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

