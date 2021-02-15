
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
## Getting a Vula site tool object ## (Toolname --> Tests, Announcements)
Vula_site_tool = Toolname(Vula_site.go_to_tool('Toolname'))

    <<<<<<<<<<Vula site tool methods>>>>>>>>>>
    1. get_all()    ---> list       (returns site content in a string list)


## DATABASES ##

                             ______________________________
>>>> GRADEBOOK TABLE        |Course | Title | Mark | Total |
                            |-------|-------|------|-------|
                            |       |       |      |       |
                             __________________________
>>>> ASSIGNMENTS TABLE      | Course | Title | Duedate |
                            |--------|-------|---------|
                            |        |       |         |

                             _______________________
>>>> ANNOUNCEMENTS TABLE    | Title | Author | Data |
                            |-------|--------|------|
                            |       |        |      |

                       _____________________________________       
>>>> TESTS TABLE      | Course | Title | Timelimit | Duedate|
                      |--------|-------|-----------|--------|
                      |        |       |           |        |
                      
#LESS IMPORTANT TABLES

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
