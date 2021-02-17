
>>>>Scraper usage<<<<

## Loggin in to vula ##
s = Scrape("userName", "passWord")

## Getting a Vula object ##
Vula = Vula = Site(s)
    
    <<<<<<<<Vula methods>>>>>>>
    1. get_sites()   ---> list
    2. go_to_site("site_name") ---> soup, session

## Getting a Vula site object ##
vula_site = SiteTool(Vula.go_to_site("vula_site_name"))

    <<<<<<<<vula_site_methods>>>>>>
    1. get_tools() ---> list
    2. go_to_tool("tool_name") ---> soup, session
## Getting a Vula site tool object ## (Toolname --> Tests, Announcements...)
Vula_site_tool = Toolname(Vula_site.go_to_tool('Toolname'))

    <<<<<<<<<<Vula site tool methods>>>>>>>>>>
    1. get_all()    ---> list       (returns site content in a string list)

# Getting all sites to be scrapped : 

    sites = Vula.get_scraping_sites()      

        [Key: site_name , Value: SiteTool object]

# Getting all sites with announcements:

    sites = Vula.with_announcements()  
    
        [Key: site_name , Value: SiteTool object]

# Getting all sites with assignments:

    sites = Vula.with_assignments()
        [Key: site_name , Value: SiteTool object]

# Getting all sites with Tests:

    sites = Vula.with_tests()
        [Key: site_name , Value: SiteTool object]

# Getting all sites with Gradebook:

    sites = Vula.with_gradebook()
        [Key: site_name , Value: SiteTool object]

# Getting all assignments from all sites with assignments
    # E.g
    for site_name in Vula.with_assignments:
        assignments = Vula.with_assignments[site_name].get_assignments()
        for assignment in assignments:
            print(assignment)
        print()

# Getting all gradebooks from all sites with gradebooks
    # E.g
    for site_name in Vula.with_gradebook:
        grades = Vula.with_gradebook[site_name].get_gradebook()
        for grade in grades:
            print(grade)
        print()

# Getting all tests from all sites wites tests and quizes
    # E.g
    for site_name in Vula.with_tests():
        print("Scraping ", site_name )
        tests = Vula.with_tests()[site_name].get_tests()
        if tests:
            print("The tests from ", site_name, " site")
            for test in tests:
                print(test)
            print()
        else:
            continue

# sites = Vula.with_assignments()
    # tests = sites["MAM1000W (2020)"].get_assignments()
    # for test in tests:
    #     print(test)


## DATABASES

                           
                         
>>>> GRADEBOOK TABLE

|Course | Title | Mark | Total |
|-------|-------|------|-------|
|       |       |      |       |
                            
                            
>>>> ASSIGNMENTS TABLE      

| Course | Title | Duedate | 
|--------|-------|---------|
|        |       |         |

                            
>>>> ANNOUNCEMENTS TABLE   

| Title | Author | Date | link |
|-------|--------|------|------|
|       |        |      |      |

                     
>>>> TESTS TABLE      

| Course | Title | Timelimit | Duedate|
|--------|-------|-----------|--------|
|        |       |           |        |
                      
## OTHER TABLES

-------------------------------------------------------------------------------
>>> Courses With Assignments Announcements Tests and the Gradebook
-------------------------------------------------------------------------------
>>> Courses With Assignemnts
-------------------------------------------------------------------------------
>>> Courses with Announcements
-------------------------------------------------------------------------------
>>> Courses with Tests
-------------------------------------------------------------------------------
>>> Courses with Gradebook
-------------------------------------------------------------------------------


## Add sites with assignements to the AssignmentSites table
>>>Create the table object
    assignementsTable  = AssignmentSitesTable()

>>>>>>Add sites
    sites = Vula.with_assignments()
    for site_name in sites:
        assignementsTable.add_site(site_name)

## Add sites with announcements to the AnouncementSites table
>>> Create the table object
    announcementsTable  = AnouncementSitesTable()

>>>>>>>Add sites
    sites = Vula.with_announcements()
    for site_name in sites:
        announcementsTable.add_site(site_name)

## Add sites with tests and quizzes to the TestSites table
>>>Create the table object
    testsTable  = TestSitesTable()

>>>>>>Add sites
    sites = Vula.with_tests()
    for site_name in sites: 
        testsTable.add_site(site_name)

## Add sites with Gradebook to the GradebookSitesTable
>>>Create the table object
    gradebooksitsTable  = GradebookSitesTable()

>>>>>>Add sites
    sites = Vula.with_gradebook()
    for site_name in sites: 
        gradebooksitsTable.add_site(site_name)