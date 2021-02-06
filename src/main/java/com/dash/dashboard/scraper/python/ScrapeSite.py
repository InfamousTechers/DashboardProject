"""
Scrape data(soup) from returned data from loginScape
and return Assignment data
"""

from loginScrape import Scrape
from bs4 import BeautifulSoup

class Site:
    def __init__(self, scraper):
        self.soup , self.session = scraper.login()
        self.sites = []
    
    def get_sites(self):
        titles = self.soup.findAll("span", {"class" : "fullTitle"})
        for title in titles:
            self.sites.append(title.string)
        return self.sites

    def site_in_sites(self, site_name):
        sites = self.get_sites()
        for site in sites:
            if site == site_name:
                return True
        return False
    
    def get_site_link(self, site_name):
        if self.site_in_sites(site_name):
            try:
                attributes = {"title": site_name}
                link = self.soup.findAll("a", attributes)
                return link[0]["href"] 
            except:
                print("there was an exception")

    def go_to_site(self, site_name):
        link = self.get_site_link(site_name)
        try:
            site = self.session.get(link)
            soup = BeautifulSoup(site.text, "html.parser")
            return soup, self.session
        except:
            pass
