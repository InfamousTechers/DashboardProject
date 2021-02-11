

from loginScrape import Scrape
from ScrapeSite import Site
from ScrapeSiteTools import SiteTool
from tools import Announcements, Tests


# Loging in
s = Scrape("student number", "password")

Vula = Site(s)

# Getting all sites to be scrapped
sites_to_scrape = Vula.get_scraping_sites() # [Key: site_name , Value: SiteTool object]

# Getting all sites with announcements
sites_with_announcements = Vula.with_announcements() # [Key: site_name , Value: SiteTool object]

# Getting all sites with assignments
sites_with_assignments = Vula.with_assignments() # [Key: site_name , Value: SiteTool object]

# Getting all sites with Tests
sites_withs_tests = Vula.with_tests() # [Key: site_name , Value: SiteTool object]

# Getting all sites with Gradebook
sites_with_gradebook = Vula.with_gradebook() # [Key: site_name , Value: SiteTool object]

 