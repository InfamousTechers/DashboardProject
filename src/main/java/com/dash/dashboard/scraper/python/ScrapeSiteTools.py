
from bs4 import BeautifulSoup
from tools import Announcements, Assignments, Gradebook, Tests

class SiteTool:
    def __init__(self, site_soup_and_session):
        try:
            self.soup , self.session = site_soup_and_session
            self.tools = []
        except:
            pass

    def get_tools(self):
        try:
            titles = self.soup.findAll("div", {"class": "Mrphs-toolsNav__menuitem--title"})
            for title in titles:
                self.tools.append(title.string)
            return self.tools
        except:
            pass

    def tool_in_tools(self, tool_name):
        tools = self.get_tools()
        try:
            for tool in tools:
                if tool == tool_name:
                    return True
        except:
            pass
        return False

    def get_tool_link(self, tool_name):
        tool_subsites_container = self.soup.find("div", {"id": "toolSubsitesContainer"})
        tools_ul = tool_subsites_container.find("ul")
        tools_lis = tools_ul.findAll("li")
        for li in tools_lis:
            try:
                if li.find("a")["title"].split("-")[0].strip() == tool_name:
                    return li.find("a")["href"]
            except:
                pass
        return -1

    def go_to_tool(self, tool_name):
        link = self.get_tool_link(tool_name)
        try:
            site = self.session.get(link)
            soup = BeautifulSoup(site.text,"html.parser")
            return soup, self.session
        except:
            pass

    def has_announcements(self):
        return self.tool_in_tools('Announcements')

    def get_announcements(self):
        announcemnts = Announcements(self.go_to_tool('Announcements'))
        return announcemnts.get_all()

    def has_assignments(self):
        return self.tool_in_tools('Assignments')

    def get_assignments(self):
        assignments = Assignments(self.go_to_tool('Assignments'))
        return assignments.get_all()

    def has_tests(self):
        return self.tool_in_tools('Tests & Quizzes')

    def get_tests(self):
        tests = Tests(self.go_to_tool('Tests & Quizzes'))
        return tests.get_all()

    def has_gradeBook(self):
        return self.tool_in_tools('Gradebook')

    def get_gradebook(self):
        if self.has_gradeBook():
            gradebook = Gradebook(self.go_to_tool('Gradebook'))
            return gradebook.get_all()
        else:
            print("there is no gradebook")