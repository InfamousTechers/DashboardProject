

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

    print(config.updateSitesTables())

    print("Getting Annouments...")
    if config.updateAnnouncementsTable():
        config.printAnnouncements()
        print()
    else:
        print("Failed to get AnnouncementsTable!!")

    print("Getting AssignmentsTable...")
    if config.updateAssignmentsTable():
        config.printAssignments()
        print()
    else:
        print("Failed to get AssignmentsTable!!")
        
    print("Getting tests...")
    if config.updateTestsTable():
        config.printTests()
        print()
    else:
        print("Failed to get tests!!!")
        
    print("Getting gradebook...")
    if config.updateGradebook():
        config.printGradebook()
        print()
    else:
        print("Print failed to get gradebook!!")


if __name__ == "__main__":
    main()
