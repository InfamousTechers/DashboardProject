

from loginScrape import Scrape
from ScrapeSite import Site
from ScrapeSiteTools import SiteTool
from tools import Announcements, Tests

# Loging in
try:
    s = Scrape("student number", "password")

    Vula = Site(s.login())
    # Getting all sites to be scrapped : Vula.get_scraping_sites()      #--> [Key: site_name , Value: SiteTool object]

    # Getting all sites with announcements: Vula.with_announcements()   #--> [Key: site_name , Value: SiteTool object]

    # Getting all sites with assignments: Vula.with_assignments()       #--> [Key: site_name , Value: SiteTool object]

    # Getting all sites with Tests: Vula.with_tests()                   #--> [Key: site_name , Value: SiteTool object]

    # Getting all sites with Gradebook: Vula.with_gradebook()           #--> [Key: site_name , Value: SiteTool object]

    # Getting all assignments from all sites with assignments
    # E.g
    for site_name in Vula.with_assignments:
        assignments = Vula.with_assignments[site_name].get_assignments()
        for assignment in assignments:
            print(assignment)
        print()

    # Getting all gradebooks from all sites with gradebooks
    # E.g
    for site_name in Vula.with_gradebook:
        print("The gradebook for ", site_name, " course.")
        grades = Vula.with_gradebook[site_name].get_gradebook()
        for grade in grades:
            print(grade)
        print()

    # Getting all tests from all sites wites tests and quizes
    # E.g
    for site_name in Vula.with_tests():
        print("Scraping ", site_name )
        tests = Vula.with_tests()[site_name].get_tests()
        if tests:
            print("The tests from ", site_name, " site")
            for test in tests:
                print(test)
            print()
        else:
            continue

    # sites = Vula.with_assignments()
    # tests = sites["MAM1000W (2020)"].get_assignments()
    # for test in tests:
    #     print(test)

except:
    print("Please check your internet connection!!!")

