
class Announcements:
    def __init__(self, announcements_soup):
        self.soup , self.session = announcements_soup
        self.announcements_list = []

    def get_all(self):
        self.get_announcements()
        return self.announcements_list[:len(self.announcements_list)-1]

    def print_soup(self):
        print(self.soup.prettify())

    def get_table(self):
        try:
            table = self.soup.find("table", {"class":"table table-hover table-striped table-bordered"})
        except:
            pass
        return table
    
    def get_announcements(self):
        try:
            table = self.get_table()
            body = table.findAll("tr")
            i = 1
            for head in body:
                days_announcements = []
                try:
                    head    = body[i].find("th")
                    auther  = body[i].findAll("td")[0]
                    date    = body[i].findAll("td")[1]
                    i += 1
                    try:
                        a_tag = head.find("a")
                        announcements_link = a_tag["href"]
                        preview = a_tag.find("span")
                        days_announcements.append(preview.string.strip())
                        days_announcements.append(auther.string.strip())
                        days_announcements.append(date.string.strip())
                        days_announcements.append(announcements_link)
                    except:
                        pass
                except:
                    pass
                self.announcements_list.append(days_announcements)
        except:
            pass

    def __str__(self):
        string = ""
        ls = self.get_all()
        for announcement in ls:
            string = string + announcement + "\n"
        return string

class Tests:
    def __init__(self, tests_soup):
        self.soup, self.session = tests_soup
        self.tests_list = []

    def get_all(self):
        self.get_tests()
        return self.tests_list

    def print_soup(self):
        print(self.soup.prettify())

    def get_table(self):
        try:
            table = self.soup.find("table", {"id" : "selectIndexForm:selectTable"})
            table = table.find("tbody")
            return table
        except:
            pass

    def get_tests(self):
        table = self.get_table()
        try:
            trows = table.findAll("tr")
            for trow in trows:
                row = []
                title = trow.find("span", {"class":"spanValue"}).string
                row.append(title)
                timelimit = trow.find("span", {"class":"currentSort"}).string
                row.append(timelimit)
                duedate = trow.find("td", {"class":"sorting_1"})
                if duedate == None:
                    duedate = 'n/a'
                else:
                    duedate = duedate.string
                row.append(duedate)
                self.tests_list.append(row)
        except:
            pass

    
    # def get_tests(self):
    #     table = self.get_table()
    #     try:
    #         rows        = table.findAll("tr")
    #         name        = table.findAll("span", {"class":"spanValue"})
    #         time_limit  = table.findAll("span" , {"class":"currentSort"})
    #         # due_date    = table.findAll("td" , {"class":"sorting_1"}) #TODO: get due date
    #         for i in range(len(name)):
    #             self.tests_list.append(f"{name[i].string}    |    {time_limit[i].string}      | ------to get the Due date")
    #             i += 1
    #     except:
    #         pass
    
    def __str__(self):
        string = ""
        ls = self.get_all()
        for test in ls:
            string = string + test + "\n"
        return string

class Assignments:
    def __init__(self, assignment_soup):
        self.soup, self.session = assignment_soup
        self.assignments_list = []
    
    def get_all(self):
        self.pack_assignments()
        return self.assignments_list

    def print_soup(self):
        print(self.soup.prettify())

    def get_table(self):
        try:
            table = self.soup.find("table", {"class" : "table table-hover table-striped table-bordered"})
            table = table.find("tbody")
            return table
        except:
            pass
        
    
    def pack_assignments(self):
        rows = self.soup.findAll("tr")
       
        for row in rows: 
            rowlst = []
            try:
                title = row.find("a", {"name":"asnActionLink"})["title"]
                dueDate = (row.find("td", {"headers":"dueDate"})).find("span", {"class":"highlight"}).string
                rowlst.append(title)
                rowlst.append(dueDate)
                self.assignments_list.append(rowlst)

            except:
                pass

class Gradebook:
    def __init__(self, gradebook_soup):
        self.soup, self.session = gradebook_soup
        self.gradebook_list = []
    
    def get_all(self):
        self.pack_gradebook()
        return self.gradebook_list
   
    def pack_gradebook(self):
        try:
            table = self.soup.find("tbody", {"class":"gb-summary-assignments-tbody"})
            rows = table.findAll("tr")
            for row in rows:
                grade = []
                title = row.find("span", {"class":"gb-summary-grade-title"}).string
                grade.append(title)
                mark = row.find("span", {"class":"gb-summary-grade-score-raw"}).string
                grade.append(mark)
                out_of = row.find("span", {"class":"gb-summary-grade-score-outof"}).string
                grade.append(out_of)
                self.gradebook_list.append(grade)
        except:
            pass