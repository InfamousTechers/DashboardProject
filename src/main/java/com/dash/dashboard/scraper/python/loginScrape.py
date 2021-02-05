"""
Python script to login to Vula 
Usage: python loginScrape.py USERNAME PASSWORD
"""

import requests
from bs4 import BeautifulSoup

class Scrape:
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
                return soup
            except:
                pass