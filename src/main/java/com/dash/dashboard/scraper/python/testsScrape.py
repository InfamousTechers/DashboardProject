"""
Scrape data(soup) from returned data from loginScape
and return Tests data

USAGE:
    ****import loginScrape****

    user = loginScrape.Scrape(USERNAME, PASSWORD)
    soup, session = user.login()
    sites = user.getSites(soup, session)

"""

from bs4 import BeautifulSoup

def testsScrape(sites, session):
    
    return 