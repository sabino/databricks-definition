# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='databricks-definition',
    version='0.1.0',
    description='Coordinate Databricks Clusters creation, permissions and libraries',
    long_description=readme,
    author='Felipe Sabino',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

