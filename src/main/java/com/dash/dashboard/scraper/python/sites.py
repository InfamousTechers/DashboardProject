
from datetime import date
from bs4 import BeautifulSoup
from databases import Database

class Site:
    def __init__(self, soup_n_session):
        # self.year = date.today().year
        self.year = 2020
        self.soup, self.session = soup_n_session
        self.database = Database()

    def go_to_link(self, link, session):
        try:
            site = session.get(link)
            soup = BeautifulSoup(site.text, "html.parser")
            return soup, self.session
        except:
            return None, None

    def getAnnouncements(self, course_name, announcements_soup):
        if announcements_soup != None:									
            try:
                table = announcements_soup.find("table", {"class" : "table table-hover table-striped table-bordered"})
                rows = table.findAll("tr")[1:]
                for row in rows:
                    date = row.find("td", {"headers":"date"}).string.strip()
                    subject = row.find("a")["title"]
                    author = row.find("td", {"headers":"author"}).string.strip()
                    link = row.find("a")["href"]
                    self.database.announcements_insert(subject,author,date,link)
                    
            except:
                pass
  
    def getAssignments(self, course_name ,assignments_soup):
        if assignments_soup != None:
            try:
                table = assignments_soup.find("table", {"class":"table table-hover table-striped table-bordered"})
                rows = table.findAll("tr")[1:]
                for row in rows:
                    title = row.find("a")["title"]
                    duedate = row.find("span", {"class":"highlight"}).string
                    link = row.find("a")["href"]
                    self.database.smart_assignments_insert(course_name, title, duedate, link)
                    self.database.assignments_insert(course_name, title, duedate)
            except:
                pass

    def getGradebook(self, course_name, gradebook_soup):
        if gradebook_soup != None:
            try:
                table = gradebook_soup.find("table", {"id":"gradeSummaryTable"})
                rows = table.findAll("tr")[1:]
                #TODO: test the following
                for row in rows:
                    title = row.find("span", {"class":"gb-summary-grade-title"}).string
                    score = row.find("span", {"class":"gb-summary-grade-score-raw"}).string
                    out_of = row.find("span", {"class":"gb-summary-grade-score-outof"}).string[1:]
                    self.database.gradebook_insert(course_name, title, score, out_of)
            except:
                pass

    def getTests(self, course_name, tests_soup):
        if tests_soup != None:
            table = tests_soup.find("table", {"id":"selectIndexForm:selectTable"})
            rows = table.findAll("tr")[1:]
            for row in rows:
                title = row.find("span", {"class":"spanValue"}).string.strip()
                timelimit = row.find("span", {"class":"currentSort"}).string.strip()
                duedate = row.find("td", {"class":"sorting_1"})
                if duedate == None:
                    duedate = 'n/a'
                self.database.tets_insert(title, timelimit, duedate)
                self.database.smart_tests_insert(course_name, title, timelimit, duedate)          
    
    def go_to_announcements(self, soup, session):
        try:
            link = soup.find("a", {"title" : "Announcements - For posting and viewing current, time-critical information"})["href"]
            return self.go_to_link(link, session)
        except:
            return None, None

    def go_to_assignments(self, soup, session):
        try:
            link = soup.find("a", {"title" : "Assignments - For posting, submitting, and grading assignments online"})["href"]
            return self.go_to_link(link, session)
        except:
            return None, None

    def go_to_gradebook(self, soup, session):
        try:
            link = soup.find("a", {"title":"Gradebook - For storing and computing assessment grades from Tests & Quizzes or that are manually entered."})["href"]
            return self.go_to_link(link, session)
        except:
            return None, None

    def go_to_tests(self, soup, session):
        try:
            link = soup.find("a", {"title":"Tests & Quizzes - For creating and taking online assessments"})["href"]
            return self.go_to_link(link, session)
        except:
            return None, None

    def filter(self, by, site_name):
        if by.lower() == "y":
            return str(self.year) in site_name


    def scrape(self):
        # get site name
        titles = self.soup.findAll("span", {"class" : "fullTitle"})
        for title in titles:
            site_name = title.string
            if str(self.year) in site_name:
                try:
                    # if site is a current year site get site link
                    attributes = {"title": site_name}
                    link = self.soup.findAll("a", attributes)
                    link = link[0]["href"] 
                    # got to site
                    site_soup, site_session = self.go_to_link(link, self.session)

                    #DO CONCURRENT PROGRAMMING

                    # go to announcements
                    announcements_soup, session = self.go_to_announcements(site_soup, site_session)
                    #     # get announcements
                    if announcements_soup != None:
                        self.getAnnouncements(site_name, announcements_soup)

                    # # go  to assignments
                    assignments_soup, session = self.go_to_assignments(site_soup, site_session)
                    #     #get assignments
                    if assignments_soup != None:
                        self.getAssignments(site_name, assignments_soup)
                    
                    # # go  to gradebook
                    gradebook_soup, session = self.go_to_gradebook(site_soup, site_session)
                    #     #get gradebook
                    if gradebook_soup != None:
                        self.getGradebook(site_name, gradebook_soup)

                    # go  to tests
                    tests_soup, session = self.go_to_tests(site_soup, site_session)
                        #get tests
                    if tests_soup != None:
                        self.getTests(site_name, tests_soup)

                except:
                    pass
            else:
                continue

    def print_announcements(self):
        annnouncements = self.database.getAnnouncements()
        for annnouncement in annnouncements:
            print(annnouncement)

    def print_assignments(self):
        assignments = self.database.getAssignments()
        for assignment in assignments:
            print (assignment)

    def print_tests(self):
        assignments = self.database.getTests()
        for assignment in assignments:
            print (assignment)

    def print_gradebook(self):
        assignments = self.database.getGradebook()
        for assignment in assignments:
            print (assignment)