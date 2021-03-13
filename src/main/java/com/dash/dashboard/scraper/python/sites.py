import concurrent.futures
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
from databases import Database

class Site:
    def __init__(self, soup_n_session):
        self.year = date.today().year
        self.month = date.today().month
        self.day = date.today().day
        # self.year = 2020
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
                    if self.isRecent(date, 60):
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
                    if self.isFutureDay(duedate):
                        link = row.find("a")["href"]
                        self.database.smart_assignments_insert(course_name, title, duedate, link)
                        self.database.assignments_insert(course_name, title, duedate)
                    else:
                        continue
            except:
                pass

    def getGradebook(self, course_name, gradebook_soup):
        if gradebook_soup != None:
            try:
                table = gradebook_soup.find("table", {"id":"gradeSummaryTable"})
                rows = table.findAll("tr")[1:]
                for row in rows:
                    title = row.find("span", {"class":"gb-summary-grade-title"}).string
                    score = row.find("span", {"class":"gb-summary-grade-score-raw"}).string
                    if score.strip() != "-":   
                        out_of = row.find("span", {"class":"gb-summary-grade-score-outof"}).string[1:]
                        self.database.gradebook_insert(course_name, title, score, out_of)
                    else:
                        continue
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

    def month_number(self, month):
        month_to_number = {
            'January' : 1,         
            'February' : 2,         
            'March' : 3,           
            'April' : 4,              
            'May' : 5, 
            'June' : 6,
            'July' : 7, 
            'August' : 8, 
            'September' : 9, 
            'October' : 10, 
            'November' : 11, 
            'December' : 12
            }
        return [v for k, v in month_to_number.items() if month.lower() in k.lower()][0]

    def isFutureDay(self, duedate):
        current_year = date.today().year
        current_month = date.today().month
        current_day = date.today().day

        datedue = duedate.strip()

        datedue = datedue.split(" ")

        due_date = []

        for i in datedue:
            if datedue.index(i) == 0 or datedue.index(i) == 2:
                i = int(i)
            due_date.append(i)

        if current_year > due_date[2]:
            return False
        elif current_year < due_date[2]:
            return True
        elif current_month > month_number(due_date[1]) and current_year == due_date[2]:
            return False
        elif current_month < month_number(due_date[1]) and current_year == due_date[2]:
            return True
        elif current_month == month_number(due_date[1]) and current_year == due_date[2]:
            if current_day > due_date[0]:
                return False
            elif current_day <= due_date[0]:
                return True

    def isRecent(self, announcementDate, N_DAYS_AGO):
        announcementDate = announcementDate.strip()
        announcementDate = announcementDate.split("-")
        announcementDate[0] = int(announcementDate[0])
        yearAndTime = announcementDate[-1]
        yearAndTime = yearAndTime.split()
        announcementDate[-1] = int(yearAndTime[0])
        announcementDate.append(yearAndTime[1])

        today = datetime.now()    
        n_days_ago = today - timedelta(days=N_DAYS_AGO)

        n_days_ago_day = n_days_ago.day
        n_days_ago_month = n_days_ago.month
        n_days_ago_year = n_days_ago.year

        current_year = date.today().year
        current_month = date.today().month
        current_day = date.today().day

        if (announcementDate[2] == current_year or announcementDate[2] == n_days_ago_year):
            if (self.month_number(announcementDate[1]) == current_month or (self.month_number(announcementDate[1]) - n_days_ago_month == 1)):
                return True
        else:
            return False

        # if announcementDate[2] < current_year:
        #     return False
        # elif (announcementDate[2] == current_year or announcementDate[2] == n_days_ago_year) and (month_number(announcementDate[1]) >= n_days_ago_month or (month_number(announcementDate[1]) == current_month and announcementDate[0] >= n_days_ago_day)):
        #     return True
        # elif announcementDate[2] == current_year and month_number(announcementDate[1]) >= n_days_ago_month and announcementDate[0] >= n_days_ago_day:
        #     return True
        # elif  announcementDate[2] == current_year and month_number(announcementDate[1]) < n_days_ago_month:
        #     return False

    def scrape(self):
        # get site name
        titles = self.soup.findAll("span", {"class" : "fullTitle"})
        for title in titles:
            site_name = title.string
            try:
                # if site is a current year site get site link
                attributes = {"title": site_name}
                link = self.soup.findAll("a", attributes)
                link = link[0]["href"] 
                # got to site
                site_soup, site_session = self.go_to_link(link, self.session)

                #DO CONCURRENT PROGRAMMING

                # # go to announcements
                announcements_soup, session = self.go_to_announcements(site_soup, site_session)
                # #     # get announcements
                if announcements_soup != None:
                    self.getAnnouncements(site_name, announcements_soup)
                
                # with concurrent.futures.ProcessPoolExecutor() as executor:
                #     f1 = executor.submit(getAnnouncements,(site_name, announcements_soup))

                # # # go  to assignments
                assignments_soup, session = self.go_to_assignments(site_soup, site_session)
                # #     #get assignments
                if assignments_soup != None:
                    self.getAssignments(site_name, assignments_soup)
                
                # # # go  to gradebook
                gradebook_soup, session = self.go_to_gradebook(site_soup, site_session)
                # #     #get gradebook
                if gradebook_soup != None:
                    self.getGradebook(site_name, gradebook_soup)

                # go  to tests
                tests_soup, session = self.go_to_tests(site_soup, site_session)
                    #get tests
                if tests_soup != None:
                    self.getTests(site_name, tests_soup)

            except:
                pass

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