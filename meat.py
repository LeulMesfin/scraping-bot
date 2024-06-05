import requests, re
from bs4 import BeautifulSoup
# main file used to practice web scraping
# site url: https://realpython.com/beautiful-soup-web-scraper-python/

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
job_info_lst = soup.find_all("div", class_="card-content")

res = soup.find(id="ResultsContainer")

python_jobs = res.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_elt in python_job_elements:
  links = job_elt.find_all("a", string="Apply")
  #print(links)
  for link in links:
    link_url = link["href"]
    print(f"Apply here: {link_url}\n")

