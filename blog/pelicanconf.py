# Thanks to SamiE for Pelican's best-looking blog theme:
# https://github.com/aleylara/Peli-Kiera

THEME = "themes/peli_kiera"

AUTHOR = "Justin Delcroix"
SITENAME = "Saved by the Junk DLC"
SITEURL = "https://tundish.github.io/junkdlc"
SITELOGO = "img/junkdlc_sketch_headshot.jpg"
COPYRIGHT = "2024"
SITESUBTITLE =" Rebuilding civilisation using only what's lying around."
PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"

STATIC_PATHS = ["images"]

ARTICLE_ORDER_BY = "date"
# Article summary length on main index page
SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10
GITHUB_URL = "https://github.com/tundish/junkdlc"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widget
SOCIAL = (
    ("odysee", "https://odysee.com/@JunkDLC:4"),
    ("tumblr", "https://junkdlc.tumblr.com/"),
)
