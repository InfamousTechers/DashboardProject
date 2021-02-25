
from databases import AnnouncementsTable, AnouncementSitesTable, AssignmentSitesTable, AssignmentsTable, GradebookSitesTable, GradebookTable, TestSitesTable, TestTable

class Configuration:
    def __init__(self, Vula):
        self.vula = Vula

        self.assignments_sites_table    = AssignmentSitesTable()
        self.announcements_sites_table  = AnouncementSitesTable()
        self.tests_sites_table          = TestSitesTable()
        self.gradebook_sites_table      = GradebookSitesTable()

        self.assignments_table          = AssignmentsTable()
        self.annnouncements_table       = AnnouncementsTable()
        self.tests_table                = TestTable()
        self.gradebook_table            = GradebookTable()
        
    def updateSitesTables(self):
        try:
            sites = self.vula.with_assignments()
            for site_name in sites:
                self.assignment_sites_table.add_site(site_name)

            sites = self.vula.with_announcements()
            for site_name in sites:
                self.announcement_sites_table.add_site(site_name)

            sites = self.vula.with_tests()
            for site_name in sites: 
                self.tests_sites_table.add_site(site_name)

            sites = self.vula.with_gradebook()
            for site_name in sites: 
                self.gradebook_sites_table.add_site(site_name)

            return True
        except:
            return False
        
    def printSitesTables(self):
        assignmentsTable = self.assignments_table.list_sites()
        for site in assignmentsTable:
            print(assignmentsTable[site])
        print()

        announcementsTable = self.announcements_table.list_sites()
        for site in announcementsTable:
            print(announcementsTable[site])
        print()

        testsTable = self.tests_table.list_sites()
        for site in testsTable:
            print(testsTable[site])
        print()

        gradebookTable = self.gradebooksits_table.list_sites()
        for site in gradebookTable:
            print(gradebookTable[site])
        print()

    def updateAnnouncementsTable(self):
        sites = self.vula.with_announcements()
        try:
            for site_name in sites:
                announcements = sites[site_name].get_announcements()
                for announcement in announcements:
                    self.annnouncements_table.insert_list(announcement)
            return True
        except:
            return False

    def printAnnouncements(self):
        announcements = self.annnouncements_table.list_content()

        for announcement in announcements:
            print(announcements[announcement])

    def updateAssignmentsTable(self):
        sites = self.vula.with_assignments()
        try:
            for site_name in sites:
                assignments = sites[site_name].get_assignments()
                for assignment in assignments:
                    assignment.insert(0, site_name)
                    self.assignments_table.insert_list(assignment)
            return True
        except:
            return False
    
    def printAssignments(self):
        assignments = self.assignments_table.list_content()

        for assignment in assignments:
            print(assignments[assignment])

    def updateTestsTable(self):
        sites = self.vula.with_tests()
        try:
            for site_name in sites:
                tests = sites[site_name].get_tests()
                for test in tests:
                    self.tests_table.insert_list(test)
            return True
        except:
            return False

    def printTests(self):
        tests = self.tests_table.list_content()

        for test in tests:
            print(tests[test])

    def updateGradebook(self):
        sites = self.vula.with_gradebook()
        try:
            for site_name in sites:
                grades = sites[site_name].get_gradebook()
                for grade in grades:
                    grade.insert(0, site_name)
                    self.gradebook_table.insert_list(grade)
                    
            return True
        except:
            return False
    
    def printGradebook(self):
        grades = self.gradebook_table.list_content()

        for grade in grades:
            print(grades[grade])