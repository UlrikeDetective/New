from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd

my_url = "https://realpython.github.io/fake-jobs/"
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")

filename = "jobs.csv"
f = open(filename, "w", encoding="utf-8")

containers = page_soup.findAll("div", {"class": "card-content"})

headers = "Job,Company,City,State,Date\n"
f.write(headers)

for container in containers:
    job = container.find("h2", {"class": "title"}).text.strip() if container.find("h2", {"class": "title"}) else 'N/A'
    company = container.find("h3", {"class": "company"}).text.strip().replace(",", "|") if container.find("h3", {"class": "company"}) else 'N/A'
    location = container.find("p", {"class": "location"}).text.strip().split(", ") if container.find("p", {"class": "location"}) else ['N/A', 'N/A']
    city = location[0]
    state = location[1] if len(location) > 1 else 'N/A'
    date = container.find("p", {"class": "date"}).text.strip() if container.find("p", {"class": "date"}) else 'N/A'
    
    f.write(f'"{job}","{company}","{city}","{state}","{date}"\n')

f.close()

jobs = pd.read_csv("jobs.csv", encoding="utf-8")
jobs.rename(columns={"Date": "State"}, inplace=True)  # Correcting the column label from Date to State
jobs['State'] = pd.to_datetime(jobs['State'], errors='coerce')  # Converting 'State' column to datetime format
jobs.to_csv("jobs_fixed.csv", index=False)  # Writing the corrected data to a new CSV file

jobs_fixed = pd.read_csv("jobs_fixed.csv", encoding="utf-8")
jobs_fixed.head()



