
>>>>Scraper usage<<<<

## Loggin in to vula ##
s = Scrape("userName", "passWord")

## Getting a Vula object ##
Vula = Vula = Site(s)
    
    <<<<<<<<Vula methods>>>>>>>
    1. get_sites() ---> list
    2. go_to_site("site_name") ---> soup, session

## Getting a Vula site object ##
vula_site = SiteTool(Vula.go_to_site("vula_site_name"))

    <<<<<<<<vula_site_methods>>>>>>
    1. get_tools() ---> list
    2. go_to_tool("tool_name") ---> soup, session



