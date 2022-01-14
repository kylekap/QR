# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='example',
    version='0.0.1',
    description='Basic package outline for projects',
    long_description=readme,
    author='Kyle Patterson',
    url='https://github.com/kylekap/TemplatePython',
    license=license,
    packages=find_packages(exclude=('Tests', 'Docs', 'Results'))
)

