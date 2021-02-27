from loginScrape import Scrape
from ScrapeSite import Site
from ScrapeSiteTools import SiteTool
from databases import AnouncementSitesTable, AssignmentSitesTable, AssignmentsTable, GradebookSitesTable, TestSitesTable
from tools import Announcements, Tests
from configuration import Configuration


def main():
    # Loging in
    studentnumber = input("Enter your student number: ")
    password = input("Enter your password: ")
    s = Scrape(studentnumber, password)
    print("logging you in... ")
    Vula = Site(s.login())

    config = Configuration(Vula)

    # if config.updateAnnouncementsTable():
    #     config.printAnnouncements()

    # if config.updateAssignmentsTable():
    #     config.printAssignments()

    # if config.updateGradebook():
    #     config.printGradebook()
    
    # if config.updateTestsTable():
    #     config.printTests()

    if input("Refresh all? [y/n]: ").lower() == "y":
        print("Fetching your data from Vula....")
        config.updateAnnouncementsTable()
        config.updateAssignmentsTable()
        config.updateTestsTable()
        config.updateGradebook()

    elif input("Refresh Announcements? [y/n]: ").lower() == "y":
        print("Fetching your Announcements from Vula....")
        config.updateAnnouncementsTable()

    elif input("Refresh Assignments? [y/n]: ").lower() == "y":
        print("Fetching Assignments from Vula....")
        config.updateAssignmentsTable()

    elif input("Refresh Tests? [y/n]: ").lower() == "y":
        print("Fetching your Tests from Vula....")
        config.updateTestsTable()

    elif input("Refresh Gradebook? [y/n]: ").lower() == "y":
        print("Fetching your Gradebook from Vula....")
        config.updateGradebook()
    

    # print(config.updateSitesTables())

    if input("Print Announcements? [y/n]: ").lower() == "y":
        print("Printing Announcements...")
        config.printAnnouncements()
        print()
    if input("Print Assignments [y/n]").lower() == "y":
        print("Printing Assignments...")
        config.printAssignments()
        print()

    if input("Print tests? [y/n]").lower() == "y":
        print("Printing tests...")
        config.printTests()
        print()
    if input("Print gradebook? [y/n]").lower() == "y":
        print("Printing gradebook...")
        config.printGradebook()
        print()

if __name__ == "__main__":
    main()
