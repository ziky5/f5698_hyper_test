"""Sphinx configuration."""
project = "F5698_Hyper_Test"
author = "Petr Zikan"
copyright = "2022, Petr Zikan"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
