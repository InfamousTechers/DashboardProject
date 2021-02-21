import sqlite3
from loginScrape import Scrape
from ScrapeSite import Site

class VulaDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("Vula.db")
        self.cursor = self.connection.cursor()

    def list_sites(self): # --> dictionary
        sites = {}
        rows = self.get_sites()
        for row in rows:
            sites[row[0]] = row[1]
        self.close_connection()
        return sites

    def close_connection(self):
        self.connection.commit()
        self.connection.close()
    
class TestSitesTable(VulaDatabase):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TestSites(id integer PRIMARY KEY, SiteName text UNIQUE NOT NULL)''')
        self.connection.commit()

    def add_site(self, site_name):
        try:
            command = "INSERT INTO TestSites (SiteName) VALUES(?)"
            self.cursor.execute(command, (site_name,))
            self.connection.commit()
        except:
            pass

    def get_sites(self):
        self.cursor.execute("SELECT * FROM TestSites")
        return self.cursor.fetchall()

class GradebookSitesTable(VulaDatabase):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS GradebookSites(id integer PRIMARY KEY, SiteName text UNIQUE NOT NULL)''')
        self.connection.commit()

    def add_site(self, site_name):
        try:
            command = "INSERT INTO GradebookSites (SiteName) VALUES(?)"
            self.cursor.execute(command, (site_name,))
            self.connection.commit()
        except:
            pass

    def get_sites(self):
        self.cursor.execute("SELECT * FROM GradebookSites")
        return self.cursor.fetchall()

class AssignmentSitesTable(VulaDatabase):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS AssignmentSites(id integer PRIMARY KEY, SiteName text UNIQUE NOT NULL)''')
        self.connection.commit()

    def add_site(self, site_name):
        try:
            command = "INSERT INTO AssignmentSites (SiteName) VALUES(?)"
            self.cursor.execute(command, (site_name,))
            self.connection.commit()
        except:
            pass

    def get_sites(self):
        self.cursor.execute("SELECT * FROM AssignmentSites")
        return self.cursor.fetchall()
    
class AnouncementSitesTable(VulaDatabase):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS AnouncementSites(id integer PRIMARY KEY, SiteName text UNIQUE NOT NULL)''')
        self.connection.commit()

    def add_site(self, site_name):
        try:
            command = "INSERT INTO AnouncementSites (SiteName) VALUES(?)"
            self.cursor.execute(command, (site_name,))
            self.connection.commit()
        except:
            pass

    def get_sites(self):
        self.cursor.execute("SELECT * FROM AnouncementSites")
        return self.cursor.fetchall()

class ToolsDb: 
    def __init__(self):
        try:
            self.connection = sqlite3.connect("VulaTools.db")
            self.cursor = self.connection.cursor()
        except:
            pass

    def list_content(self): #--> dictionary
        contents = {}
        rows = self.get_content()
        for row in rows:
            ls = []
            ls.append(row[1])
            ls.append(row[2])
            ls.append(row[3])
            ls.append(row[4])
            contents[row[0]] = ls
        self.connection.close()
        return contents

    def close_connection(self):
        self.connection.commit()
        self.connection.close()

class AnnouncementsTable(ToolsDb):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS AnnouncementsTable
        (id integer PRIMARY KEY, Preview text UNIQUE NOT NULL, Author text NOT NULL, Date text NOT NULL, Link text NOT NULL)''')
        self.connection.commit()

    def insert(self, preview, author, date, link):
        try:
            sqlite_insert_with_param = """INSERT INTO AnnouncementsTable
                            (Preview, Author, Date, Link) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (preview, author, date, link)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def insert_list(self, my_list):
        preview = my_list[0]
        author = my_list[1]
        date = my_list[2]
        link = my_list[3]
        self.insert(preview, author, date, link)

    def get_content(self):
        self.cursor.execute("SELECT * FROM AnnouncementsTable")
        return self.cursor.fetchall()            
    
class TestTable(ToolsDb):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TestsTable
        (id integer PRIMARY KEY, Title text UNIQUE NOT NULL, Timelimit text NOT NULL, Duedate text NOT NULL)''')
        self.connection.commit()
    
    def insert(self, title, time_limit, due_date):
        try:
            command = """ INSERT INTO TestsTable
            (Title, Timelimit, Duedate)
            VALUES (?, ?, ?);"""

            data_tuple = (title, time_limit, due_date)
            self.cursor.execute(command, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def insert_list(self, my_list):
        title = my_list[0]
        timelimit = my_list[1]
        duedate = my_list[2]
        self.insert(title, timelimit, duedate)

    def get_content(self):
        self.cursor.execute("SELECT * FROM TestsTable")
        return self.cursor.fetchall()

    def list_content(self): #--> dictionary
        contents = {}
        rows = self.get_content()
        for row in rows:
            ls = []
            ls.append(row[1])
            ls.append(row[2])
            ls.append(row[3])
            contents[row[0]] = ls
        self.connection.close()
        return contents
    
class AssignmentsTable(ToolsDb):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS AssignmentsTable
        (id integer PRIMARY KEY,Course text NOT NULL, Title text UNIQUE NOT NULL, Duedate text NOT NULL)''')
        self.connection.commit()

    def insert(self,course, title, duedate):
        try:
            sqlite_insert_with_param = """INSERT INTO AssignmentsTable
                            (Course, Title, Duedate) 
                            VALUES (?, ?, ?);"""

            data_tuple = (course, title, duedate)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def insert_list(self, my_list):
        course = my_list[0]
        title = my_list[1]
        duedate = my_list[2]
        self.insert(course, title, duedate)

    def get_content(self):
        self.cursor.execute("SELECT * FROM AssignmentsTable")
        return self.cursor.fetchall()

    def list_content(self): #--> dictionary
        contents = {}
        rows = self.get_content()
        for row in rows:
            ls = []
            ls.append(row[1])
            ls.append(row[2])
            ls.append(row[3])
            contents[row[0]] = ls
        self.connection.close()
        return contents

class GradebookTable(ToolsDb):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS GradebookTable
        (id integer PRIMARY KEY,Course text NOT NULL, Title text UNIQUE NOT NULL, Mark text NOT NULL, Total text NOT NULL)''')
        self.connection.commit()

    def insert(self, course, title, mark, total):
        try:
            sqlite_insert_with_param = """INSERT INTO GradebookTable
                            (Course, Title, Mark, Total) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (course, title, mark, total)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def insert_list(self, my_list):
        course = my_list[0]
        title = my_list[1]
        mark = my_list[2]
        total = my_list[3]
        self.insert(course, title, mark, total)

    def get_content(self):
        self.cursor.execute("SELECT * FROM GradebookTable")
        return self.cursor.fetchall()

    def list_content(self): #--> dictionary
        contents = {}
        rows = self.get_content()
        for row in rows:
            ls = []
            ls.append(row[1])
            ls.append(row[2])
            ls.append(row[3])
            ls.append(row[4])
            contents[row[0]] = ls
        self.connection.close()
        return contents


