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

import os
from datetime import datetime

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'marvis'
author = 'Arne Boockmeyer, Martin Michaelis, Felix Gohla'
copyright = f'{datetime.utcnow().year}, {author}'

# The full version, including alpha/beta/rc tags
version = '0.2.0'

if 'BUILD_TAG' in os.environ:
    release = os.environ['BUILD_TAG']
    if release != 'master':
        version = f'{version} - {release}'

release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_autopackagesummary",
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_copy_source = False

if 'VERSIONS_JS_URL' in os.environ:
    html_js_files = [os.environ['VERSIONS_JS_URL']]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

autodoc_default_options = {
    'member-order': 'bysource', # Include Python objects as they appear in source files
    'show-inheritance': True,
}
## Generate autodoc stubs with summaries from code
autosummary_generate = True

html_show_sphinx = False

# Link replacement
extlinks = {
    'src': ('https://github.com/diselab/marvis/tree/master/%s', 'src ')
}

# Inheritance diagram design
inheritance_graph_attrs = dict(rankdir='TB', fontsize=18)
inheritance_edge_attrs = dict(dir='back', arrowtail='empty', arrowsize=1.5)
