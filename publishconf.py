# This file is only used if you use `make publish` or
"""Pelican publish configuration."""
# explicitly specify it as your config file.

from pelicanconf import *  # noqa: F403

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://studio.kalavera.xyz"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
