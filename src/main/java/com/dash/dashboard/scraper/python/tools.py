
class Announcements:
    def __init__(self, announcements_soup):
        self.soup , self.session = announcements_soup
        self.announcements_list = []

    
    def get_all_announcements(self):
        self.get_announcements()
        return self.announcements_list[:len(self.announcements_list)-1]

    def print_soup(self):
        print(self.soup.prettify())

    def get_table(self):
        table = self.soup.find("table", {"class":"table table-hover table-striped table-bordered"})
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