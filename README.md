# XING Scraper
Scrapes XING user data. This script is loosely based on joeyisms linkedin_scraper (https://github.com/joeyism/linkedin_scraper) and utilizes Selenium and Chromedriver.

## Installation

```bash
pip3 install --user xing_scraper
```

## Setup
First, you must set your chromedriver location by

```bash
export CHROMEDRIVER=~/chromedriver
```

## Usage
To use it, just create the class

### User Scraping

```python
from xing_scraper import Person
person = Person("https://www.xing.com/profile/Max_Mustermann")
```
