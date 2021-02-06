"""
Scrape data(soup) from returned data from loginScape
and return Gradebook data

USAGE:
    ****import loginScrape****

    user = loginScrape.Scrape(USERNAME, PASSWORD)
    soup, session = user.login()
    sites = user.getSites(soup, session)
"""

from bs4 import BeautifulSoup as BS

def gradebookScrape(sites, session):
    gradebook = {}
    for site in sites:
        siteSession = session.get(site['href'])
        siteSoup = BS(siteSession.text, "html.parser")
        try:
            gradebookLink = siteSoup.find_all('a', class_ = "Mrphs-toolsNav__menuitem--link", title = "Gradebook - For storing and computing assessment grades from Tests & Quizzes or that are manually entered.")[0]['href']
            gradebookSession = session.get(gradebookLink)
            gradebookSoup = BS(gradebookSession.text, "html.parser")
            titles = gradebookSoup.find_all('span', class_ = "gb-summary-grade-title")
            grade = gradebookSoup.find_all('span', class_ = "gb-summary-grade-score-raw")
            gradeOutof = gradebookSoup.find_all('span', class_ = "gb-summary-grade-score-outof")
            grades = []
            for grd in range(len(grade)):
                grades.append(f"{titles[grd].text} | {grade[grd].text}{gradeOutof[grd].text}")
        except IndexError:
            continue

        gradebook[site.text] = grades

    return gradebook