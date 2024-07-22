"""Pelican configuration."""

AUTHOR = "Jony Kalavera"
SITENAME = "Studio Kalavera"
SITESUBTITLE = "One-man Game Development Studio"
SITEURL = "studio.kalavera.xyz"
LOGO = "/img/logo.png"

PATH = "content"

TIMEZONE = "America/Mexico_City"

DEFAULT_LANG = "en"

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM: str | None = None
CATEGORY_FEED_ATOM: str | None = None
TRANSLATION_FEED_ATOM: str | None = None
AUTHOR_FEED_ATOM: str | None = None
AUTHOR_FEED_RSS: str | None = None

LINKS: tuple[tuple[str, str], ...] = (("Github", "https://github.com/jonkalavera"),)

# Social widget
SOCIAL: tuple[tuple[str, str], ...] = tuple()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Formatting for dates

DEFAULT_DATE_FORMAT = "%d/%b/%Y %a"

# Formatting for URLs

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "neighbors", "related_posts"]


# Specify theme
THEME = "./theme/"

DISQUS_SITENAME = "studio-kalavera"
GOOGLE_ANALYTICS = "G-WLY18FTC4C"
GOOGLE_ANALYTICS_DOMAIN = "studio.kalavera.xyz"
GOOGLE_TAG_MANAGER = "GTM-W8KR5QBF"

# Plugin-specific settings

RELATED_POSTS_MAX = 20

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
