

from loginScrape import Scrape
from ScrapeSite import Site
from ScrapeSiteTools import SiteTool
from databases import AnouncementSitesTable, AssignmentSitesTable, AssignmentsTable, GradebookSitesTable, TestSitesTable
from tools import Announcements, Tests
from configuration import Configuration


def main():
    # Loging in
    studentnumber = input("Enter your student number: ")
    password = input("Enter you password: ")
    s = Scrape(studentnumber, password)
    print("logging you in... ")
    Vula = Site(s.login())

    config = Configuration(Vula)
    
    print("Fetching your data on Vula....")

    # print(config.updateSitesTables())

    if config.updateAnnouncementsTable():
        print("Printing Annouments...")
        config.printAnnouncements()
        print()

    if config.updateAssignmentsTable():
        print("Printing Assignments...")
        config.printAssignments()
        print()

    if config.updateTestsTable():
        print("Printing tests...")
        config.printTests()
        print()

    if config.updateGradebook():
        print("Printing gradebook...")
        config.printGradebook()
        print()

if __name__ == "__main__":
    main()