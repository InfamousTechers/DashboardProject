import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("VulaTools.db")
        self.cursor = self.connection.cursor()
        #Create Announcements table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Announcements
        (id integer PRIMARY KEY, Preview text UNIQUE NOT NULL, Author text NOT NULL, Date text NOT NULL,Link text NOT NULL)''')
        #Create Tests table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Tests
        (id integer PRIMARY KEY, Title text UNIQUE NOT NULL, Timelimit text NOT NULL, Duedate text NOT NULL)''')
        # Creat SmartTests if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS SmartTests
        (id integer PRIMARY KEY,Course text NOT NULL ,Title text UNIQUE NOT NULL, Timelimit text NOT NULL, Duedate text NOT NULL)''')
        #Create Assignments table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Assignments
        (id integer PRIMARY KEY,Course text NOT NULL, Title text UNIQUE NOT NULL, Duedate text NOT NULL)''')
        #Create SmartAssignments table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS SmartAssignments
        (id integer PRIMARY KEY,Course text NOT NULL, Title text UNIQUE NOT NULL, Duedate text NOT NULL, Link text)''')
        #Create gradebook table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Gradebook
        (id integer PRIMARY KEY,Course text NOT NULL, Title text UNIQUE NOT NULL, Mark text NOT NULL, Total text NOT NULL)''')

        self.connection.commit()

    def announcements_insert(self, preview, author, date,link):
        try:
            sqlite_insert_with_param = """INSERT INTO Announcements
                            (Preview, Author, Date,Link) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (preview, author, date,link)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass
    
    def assignments_insert(self,course, title, duedate):
        try:
            sqlite_insert_with_param = """INSERT INTO Assignments
                            (Course, Title, Duedate) 
                            VALUES (?, ?, ?);"""

            data_tuple = (course, title, duedate)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def smart_assignments_insert(self,course, title, duedate, link):
        try:
            sqlite_insert_with_param = """INSERT INTO Assignments
                            (Course, Title, Duedate, Link) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (course, title, duedate, link)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass


    def gradebook_insert(self, course, title, mark, total):
        try:
            sqlite_insert_with_param = """INSERT INTO Gradebook
                            (Course, Title, Mark, Total) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (course, title, mark, total)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def tets_insert(self, title, time_limit, due_date):
        try:
            command = """ INSERT INTO Tests
            (Title, Timelimit, Duedate)
            VALUES (?, ?, ?);"""

            data_tuple = (title, time_limit, due_date)
            self.cursor.execute(command, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass

    def smart_tests_insert(self, course, title, time_limit, due_date):
        try:
            command = """ INSERT INTO Tests
            (Course, Title, Timelimit, Duedate)
            VALUES (?, ?, ?, ?);"""

            data_tuple = (course, title, time_limit, due_date)
            self.cursor.execute(command, data_tuple)
            self.connection.commit()
        except sqlite3.Error as error:
            pass


    def getAnnouncements(self):
        self.cursor.execute("SELECT * FROM Announcements")
        return self.cursor.fetchall() 

    def getAssignments(self):
        self.cursor.execute("SELECT * FROM Assignments")
        return self.cursor.fetchall()

    def getGradebook(self):
        self.cursor.execute("SELECT * FROM Gradebook")
        return self.cursor.fetchall()

    def getTests(self):
        self.cursor.execute("SELECT * FROM Tests")
        return self.cursor.fetchall()