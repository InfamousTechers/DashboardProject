
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
            print("There was an exception")
        return table
    
    def get_announcements(self):
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
                    preview = a_tag.find("span")
                    days_announcements.append(preview.string.strip())
                    days_announcements.append(auther.string.strip())
                    days_announcements.append(date.string.strip())
                except:
                    pass
            except:
                pass
            self.announcements_list.append(days_announcements)

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
            rows        = table.findAll("tr")
            name        = table.findAll("span", {"class":"spanValue"})
            time_limit  = table.findAll("span" , {"class":"currentSort"})
            # due_date    = table.findAll("td" , {"class":"sorting_1"}) #TODO: get due date
            for i in range(len(name)):
                self.tests_list.append(f"{name[i].string}    |    {time_limit[i].string}      | ------to get the Due date")
                i += 1
        except:
            pass
    
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
                # print()
                title = row.find("a", {"name":"asnActionLink"})["title"]
                dueDate = (row.find("td", {"headers":"dueDate"})).find("span", {"class":"highlight"}).string
                rowlst.append(title)
                rowlst.append(dueDate)
                self.assignments_list.append(rowlst)

            except:
                pass

    
    # def __str__(self):
    #     string = ""
    #     ls = self.get_all()
    #     for test in ls:
    #         string = string + test + "\n"
    #     return string

class Gradebook:
    def __init__(self, gradebook_soup):
        self.soup, self.session = gradebook_soup
        self.gradebook_list = []
    
    def get_all(self):
        self.pack_gradebook()
        return self.gradebook_list

        
    def pack_gradebook(self):
        table = self.soup.find("tbody", {"class":"gb-summary-assignments-tbody"})
        rows = table.findAll("tr")
        for row in rows:
            title = row.find("span", {"class":"gb-summary-grade-title"}).string
            mark = row.find("span", {"class":"gb-summary-grade-score-raw"}).string
            out_of = row.find("span", {"class":"gb-summary-grade-score-outof"}).string
            self.gradebook_list.append(f"{title}    {mark}{out_of}")