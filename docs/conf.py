# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.


import os.path
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
THIS = os.path.abspath(".")
#sys.path.append(os.path.join(THIS, "../../lib/python-squirro"))

# -- Project information -----------------------------------------------------

project = "Squirro Developer Documentation"
copyright = f"{datetime.utcnow().year}, Squirro AG"
author = "Squirro AG"

# The full version, including alpha/beta/rc tags
release = "3.2.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    "sphinx.ext.autodoc",
#    "sphinx_js",
#    "sphinx_material",
#    "sphinxcontrib.mermaid",
#    "sphinxemoji.sphinxemoji",
#]

# Add any paths that contain here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# JavaScript source
#js_source_path = "../../integration"
#jsdoc_config_path = "../../integration/jsdoc.json"

# respect member order of automatically documented source code
autodoc_member_order = "bysource"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = "sphinx_material"
#html_theme_options = {
#    # Set the color and the accent color
#    "color_primary": "#E55100",
#    "color_accent": "#353535",
#    "globaltoc_depth": -1,
#    "globaltoc_collapse": True,
#    "globaltoc_includehidden": True,
#}

html_show_sphinx = False
html_copy_source = False
html_show_sourcelink = False
html_short_title = "Squirro Developer Documentation"

html_sidebars = {
    "**": [
        "globaltoc.html",
        "localtoc.html",
        "sourcelink.html",
        "searchbox.html",
    ]
}

# Which version of Mermaid to load
# TODO: This is currently always embedded - should only be used when we have a
# chart on a page.
mermaid_version = "8.8.0"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_extra_path = {"storybook": "storybook-static/index.html"}

# Custom theming for Squirro
html_logo = "_static/images/logo2.png"
html_css_files = ["css/custom.css"]

# Custom JS
html_js_files = ["js/custom.js"]
