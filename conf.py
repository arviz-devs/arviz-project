import random

# -- Project information
project = "ArviZ project"
author = "ArviZ contributors"
copyright = f"2022, {author}"

version = ""
release = version


# -- General configuration

extensions = [
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

exclude_patterns = ["Thumbs.db", ".DS_Store", ".ipynb_checkpoints", "README.md", "cards/*"]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "code"

# -- Options for extensions

myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath"]


# -- Options for HTML output

html_theme = "furo"
html_title = project
html_static_path = ["sphinx", "arviz_logos"]
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/fontawesome.min.css",
]
html_js_files = ["https://code.iconify.design/2/2.1.1/iconify.min.js"]
logo = "ArviZ.png"
html_favicon = "arviz_logos/favicon.ico"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0f718e",
        "color-brand-content": "#069fac",
    },
    "dark_css_variables": {
        "color-brand-primary": "#069fac",
        "color-brand-content": "#00c0bf",
    },
    "sidebar_hide_name": True,
    "light_logo": logo,
    "dark_logo": "ArviZ_white.png",
}

intersphinx_mapping = {"arviz": ("https://python.arviz.org/en/latest/", None)}
