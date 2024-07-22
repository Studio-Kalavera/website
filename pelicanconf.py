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
# TEMPLATE_PAGES = {"blog.html": "blog.html"}
STATIC_PATHS = ["images", "extra/CNAME"]
# EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS: tuple[tuple[str, str], ...] = tuple()

# Social widget
SOCIAL: tuple[tuple[str, str], ...] = tuple()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# PAGINATED_DIRECT_TEMPLATES = ("blog-index",)
# DIRECT_TEMPLATES = ("categories", "index", "blog-index", "blog")

# POST_LIMIT = 3

# Formatting for dates

# DEFAULT_DATE_FORMAT = "%d/%b/%Y %a"

# Formatting for urls

# ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
# ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins

# PLUGIN_PATH = "plugins"
# PLUGINS = ["sitemap", "neighbors", "related_posts"]


# Specify theme
THEME = "./theme/"
# GOOGLE_SEARCH = '013542728820335073314:dcpel18vrey'
# SWIFTYPE = ""
# SITE_THUMBNAIL = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
# SITE_THUMBNAIL_TEXT = "Studio Kalavera"

# DISQUS_SITENAME = "studio-kalavera"
GOOGLE_ANALYTICS = "G-WLY18FTC4C"
GOOGLE_ANALYTICS_DOMAIN = "studio.kalavera.xyz"
GOOGLE_TAG_MANAGER = "GTM-W8KR5QBF"

# Plugin-specific settings

# RELATED_POSTS_MAX = 20

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
