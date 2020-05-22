from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('xing_scraper/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = 'xing_scraper',
        packages = ['xing_scraper'], # this must be the same as the name above
        version = version,
        description = 'Scrapes user data from Xing',
        author = 'Sebastian Hätälä',
        author_email = 'hatala91@gmail.com',
        url = 'https://github.com/hatala91/xing_scraper', # use the URL to the github repo
        download_url = 'https://github.com/hatala91/xing_scraper/dist/' + version + '.tar.gz',
        keywords = ['xing', 'scraping', 'scraper'], 
        classifiers = [],
        install_requires=['lxml', 'request', 'selenium'],
        )
