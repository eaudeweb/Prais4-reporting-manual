# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PRAIS4 Reporting Manual'
copyright = '2021, UNCCD'
author = 'UNCCD'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'style_nav_header_background': '#ff7100',
    'collapse_navigation': False,
}

html_context = {
    "display_github": True,
    "github_user": "eaudeweb",
    "github_repo": "Prais4-reporting-manual",
    "github_version": "master",
    "conf_py_path": "/",
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'PRAIS4 Reporting Manual'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'PRAIS4'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'img/unccd_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'imag/favicon.ico'

# see https://docs.readthedocs.io/en/stable/guides/pdf-non-ascii-languages.html
latex_engine = 'xelatex'

pdf_documents = [
    ('index', u'PRAIS4_user_manual', u'PRAIS4 User Manual', u'UNCCD', '2021-06-15'),
]
