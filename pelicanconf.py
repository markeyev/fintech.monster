AUTHOR = 'Fintech Monster'
SITENAME = 'Fintech Monster'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/404.html': {'path': '404.html'},
}

TIMEZONE = 'Europe/Berlin'

ARTICLE_EXCLUDES = ['images']

DEFAULT_LANG = 'en'
LOCALE = ('en_US.UTF-8', 'en_US', 'C')
DATE_FORMATS = {
    'en': ('en_US.UTF-8', '%a, %d %b %Y'),
}
THEME = 'themes/clean-monster'

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

# Feed generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
RSS_FEED_SUMMARY_ONLY = False

# Sitemap Configuration
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.8,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "monthly"
    }
}

PLUGINS = ['sitemap']

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Twitter', '#'),
          ('LinkedIn', '#'),)

DEFAULT_PAGINATION = 10

# Dynamic Features
MARKET_TICKER = [
    ('BTC/USD', '$152,430', '+5.2%', 'text-cyber-green'),
    ('ETH/USD', '$8,200', '-1.4%', 'text-red-500'),
    ('SOL/USD', '$420', '+12%', 'text-cyber-green'),
    ('NASDAQ', '18,500', '0.0%', 'text-cyber-dim'),
    ('SPX', '5,200', '-0.5%', 'text-red-500'),
    ('MNSTR', '100.0', 'NEW', 'text-cyber-green'),
]

# AdSense (Replace with real ID)
GOOGLE_ADSENSE_ID = 'ca-pub-XXXXXXXXXXXXXXXX' # Placeholder

# Author Bios for E-E-A-T
AUTHOR_BIO = {
    "Fintech Monster Editorial": "The Fintech Monster Editorial Board is comprised of veteran financial journalists and crypto analysts dedicated to uncovering the truth behind the market's biggest moves. We prioritize facts, data, and institutional-grade analysis.",
    "Bot": "Automated market data reporter.",
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
