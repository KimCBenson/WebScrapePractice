# imports
import requests
import csv
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# if page is found, get info
if page.status_code == 200:
  soup = BeautifulSoup(page.content, 'html.parser') # parsed document
  results = soup.find(id="ResultsContainer") # find results container

  job_postings = results.find_all("div", class_="card-content") # find all job postings

  # add each job to the array used for table data
  with open("output.csv", "w", newline="") as file:
    titles = ["Job", "Company", "Location"]
    writer = csv.writer(file)

    writer.writerow(titles)

    for job in job_postings:
      title = job.find("h2", class_="title").text.strip()
      company = job.find("h3", class_="company").text.strip()
      location = job.find("p", class_="location").text.strip()
      
      job = [title, company, location]

      writer.writerow(job)

else:
  print("Page not found!")