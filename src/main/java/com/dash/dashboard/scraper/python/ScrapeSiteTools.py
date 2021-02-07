
from bs4 import BeautifulSoup

class SiteTool:
    def __init__(self, site_soup_and_session):
        self.soup , self.session = site_soup_and_session
        self.tools = []

    def get_tools(self):
        try:
            titles = self.soup.findAll("div", {"class": "Mrphs-toolsNav__menuitem--title"})
            for title in titles:
                self.tools.append(title.string)
            return self.tools
        except:
            print("Something went wrong!")

    def tool_in_tools(self, tool_name):
        tools = self.get_tools()
        for tool in tools:
            if tool == tool_name:
                return True
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
            soup = BeautifulSoup(site.text, "html.parser")
            return soup, self.session
        except:
            pass
        return -1

    
