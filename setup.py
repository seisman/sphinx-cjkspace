# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sphinx-cjkspace',
    version='0.1.2',
    description='Python extension to remove extra spaces between CJK characters',
    long_description=readme,
    author='Dongdong Tian',
    author_email='seisman.info@gmail.com',
    url='https://github.com/seisman/sphinx-cjkspace',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['sphinx', 'zhon'],
)
