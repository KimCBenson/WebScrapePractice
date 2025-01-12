# imports
import requests
import tabulate
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# if page is found, get info
if page.status_code == 200:
  table_data = [] # empty array to hold jobs in a table

  soup = BeautifulSoup(page.content, 'html.parser') # parsed document
  results = soup.find(id="ResultsContainer") # find results container

  job_postings = results.find_all("div", class_="card-content") # find all job postings

  # add each job to the array used for table data
  for job in job_postings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    
    job = [title, company, location]

    table_data.append(job)
  
  # create and print a table of all of the jobs
  job_table = tabulate.tabulate(table_data, headers=["Job", "Company", "Location"], tablefmt="grid")
  print(job_table)

else:
  print("Page not found!")