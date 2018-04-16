.. image:: https://travis-ci.org/seisman/sphinx-cjkspace.svg?branch=master
    :target: https://travis-ci.org/seisman/sphinx-cjkspace

.. image:: https://img.shields.io/github/release/seisman/sphinx-cjkspace.svg
    :target: https://github.com/seisman/sphinx-cjkspace/releases

.. image:: https://img.shields.io/pypi/v/sphinx-cjkspace.svg
    :target: https://pypi.org/project/sphinx-cjkspace/

.. image:: https://img.shields.io/github/license/seisman/sphinx-cjkspace.svg
    :target: https://github.com/seisman/sphinx-cjkspace/blob/master/LICENSE

sphinx-cjkspace
===============

A Sphinx extention that remove extra spaces between CJK characters due to
newlines in reStructuredText files.

Installation
-------------

::

    pip install sphinx-cjkspace


Usage
-----

Add it as sphinx extensions in `conf.py`:

.. code:: python

    extensions = [
        'sphinx_cjkspace.cjkspace',
    ]
