from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

my_url = "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")

filename = "imdb_m.csv"
f = open(filename, "w", encoding="utf-8")

containers = page_soup.findAll("div", {"class": "lister-item-content"})

headers = "Name, Year, Runtime\n"
f.write(headers)

for container in containers:
    name = container.a.text.strip() if container.a else 'N/A'
    year = container.find("span", {"class": "lister-item-year"}).text.strip() if container.find("span", {"class": "lister-item-year"}) else 'N/A'
    runtime = container.find("span", {"class": "runtime"}).text.strip() if container.find("span", {"class": "runtime"}) else 'N/A'
    
    f.write(f"{name}, {year}, {runtime}\n")

f.close()

import pandas as pd
imdb = pd.read_csv("imdb_m.csv", encoding="utf-8")
imdb.head()
