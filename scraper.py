# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.
 Skip to content

    Explore
    Gist
    Blog
    Help

    NaefNaef NaefNaef

    3
    3
    6

pallih/scraperwiki-scraper-vault

scraperwiki-scraper-vault / Users / T / tozzi / homegatech.py
Páll Hilmarsson pallih on 30 Sep 2013
Scrape on 30.9.2013

1 contributor
69 lines (62 sloc) 2.268 kb
import scraperwiki
from BeautifulSoup import BeautifulSoup
def scrape_table(soup):
i = 0
tds = soup.findAll('tr') # get all the <td> tags
for tr in tds:
k = 0
record = {}
tdr = tr.findAll('td') # get all the <td> tags
i = i + 1
record["i"] = i
for td in tdr:
k = k + 1
if k == 4:
record["address"] = td.text
if k == 5:
record["detail"] = td.text
if k == 6:
record["price"] = td.text
print record
scraperwiki.datastore.save(["i"], record)
def scrape_and_look_for_next_link(url):
html = scraperwiki.scrape(url)
soup = BeautifulSoup(html)
scrape_table(soup)
next_link = soup.find("a", { "class" : "forward iconLink" })
#if next_link:
# next_url = next_link['href']
# scrape_and_look_for_next_link(next_url)
starting_url = 'http://www.homegate.ch/kaufen/wohnung/bezirk-zuerich/trefferliste?a=default&tab=list&l=default&cid=3032967&aj=900000&ep=1&incsubs=default&tid=1&fromItem=ctn_zh'
scrape_and_look_for_next_link(starting_url)
import scraperwiki
from BeautifulSoup import BeautifulSoup
def scrape_table(soup):
i = 0
tds = soup.findAll('tr') # get all the <td> tags
for tr in tds:
k = 0
record = {}
tdr = tr.findAll('td') # get all the <td> tags
i = i + 1
record["i"] = i
for td in tdr:
k = k + 1
if k == 4:
record["address"] = td.text
if k == 5:
record["detail"] = td.text
if k == 6:
record["price"] = td.text
print record
scraperwiki.datastore.save(["i"], record)
def scrape_and_look_for_next_link(url):
html = scraperwiki.scrape(url)
soup = BeautifulSoup(html)
scrape_table(soup)
next_link = soup.find("a", { "class" : "forward iconLink" })
#if next_link:
# next_url = next_link['href']
# scrape_and_look_for_next_link(next_url)
starting_url = 'http://www.homegate.ch/kaufen/wohnung/bezirk-zuerich/trefferliste?a=default&tab=list&l=default&cid=3032967&aj=900000&ep=1&incsubs=default&tid=1&fromItem=ctn_zh'
scrape_and_look_for_next_link(starting_url)

    Status
    API
    Training
    Shop
    Blog
    About

    © 2014 GitHub, Inc.
    Terms
    Privacy
    Security
    Contact


