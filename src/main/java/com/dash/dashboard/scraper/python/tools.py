
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
       