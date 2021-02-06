from loginScrape import Scrape

def get_options(soup):
    options = []
    titles = soup.findAll("span", {"class" : "fullTitle"})
    for title in titles:
        options.append(title.string)
    return options


