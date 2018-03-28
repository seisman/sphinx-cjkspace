# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'sphinx-cjkspace'
author = 'Dongdong Tian'
copyright = '2018, {}'.format(author)
version = '0.1.0'
release = version


# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_cjkspace.cjkspace'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
# html_theme_options = {}
html_static_path = ['_static']
