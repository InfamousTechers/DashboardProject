"""
Python script to login to Vula 
Usage: python loginScrape.py USERNAME PASSWORD
"""

import requests
from bs4 import BeautifulSoup

class Vula:
    def __init__(self, username, password):
        self.VULA_LOGIN_URL = "https://vula.uct.ac.za/portal/xlogin"
        self.VULA_HOMEPAGE_URL = "https://vula.uct.ac.za/portal"
        self.payload = {
            'eid': username,
            'pw': password
        }

    def login(self):
        with requests.Session() as session:
            login = session.post(self.VULA_LOGIN_URL, data = self.payload)
            try:
                home = session.get(self.VULA_HOMEPAGE_URL)
                soup = BeautifulSoup(home.text, "html.parser")
                return soup, session
            except:
                pass

    def getSites(self, soup, session):
        sitesLink = soup.find_all('a', class_ = "Mrphs-toolsNav__menuitem--link")[5]['href']
        sitesPage = session.get(sitesLink)
        sitesSoup = BeautifulSoup(sitesPage.text, "html.parser")
        sites = sitesSoup.find_all('a', target = "_top")
        return sites