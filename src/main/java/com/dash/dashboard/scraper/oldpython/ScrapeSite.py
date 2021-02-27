"""
Scrape data(soup) from returned data from loginScape
and return Assignment data
"""
from bs4 import BeautifulSoup
from ScrapeSiteTools import SiteTool


class Site:
    def __init__(self, scraper):
        self.s = scraper
        self.soup , self.session = scraper
        self.sites = []
    
    def get_sites(self):
        titles = self.soup.findAll("span", {"class" : "fullTitle"})
        for title in titles:
            self.sites.append(title.string)
        return self.sites

    def get_scraping_sites(self):
        to_be_scraped = {}
        Vula = Site(self.s)
        for site_name in self.get_sites():
            site = SiteTool(Vula.go_to_site(site_name))
            if (site.has_announcements() or site.has_assignments() or site.has_gradeBook() or site.has_tests()):
                to_be_scraped[site_name] = site
        return to_be_scraped

    def with_announcements(self):
        sites = {}
        Vula = Site(self.s)
        for site_name in self.get_sites():
            site = SiteTool(Vula.go_to_site(site_name))
            if site.has_announcements():
                sites[site_name] = site
        return sites

    def with_tests(self):
        sites = {}
        Vula = Site(self.s)
        for site_name in self.get_sites():
            site = SiteTool(Vula.go_to_site(site_name))
            if site.has_tests():
                sites[site_name] = site
        return sites
    
    def with_assignments(self):
        sites = {}
        Vula = Site(self.s)
        for site_name in self.get_sites():
            site = SiteTool(Vula.go_to_site(site_name))
            if site.has_assignments():
                sites[site_name] = site
        return sites

    def with_gradebook(self):
        sites = {}
        Vula = Site(self.s)
        for site_name in self.get_sites():
            site = SiteTool(Vula.go_to_site(site_name))
            if site.has_gradeBook():
                sites[site_name] = site
        return sites

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
                pass

    def go_to_site(self, site_name):
        link = self.get_site_link(site_name)
        try:
            site = self.session.get(link)
            soup = BeautifulSoup(site.text, "html.parser")
            return soup, self.session
        except:
            pass
