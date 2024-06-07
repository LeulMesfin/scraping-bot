import requests 
from bs4 import BeautifulSoup
import re

url = "https://pythonjobs.github.io/jobs/"
page_list = ["hbk-strats-developer.html", "open-data-services-co-operative-python-software-developer.html", "oomnitza-back-end-sw-enginneer-irl-remote.html", "bmat-python-backend-engineer.html", "bmat-senior-backend-engineer.html"]

# loop thru the urls of diff pages
# print out the relevant info
# i.e:
# print out title from first page, email, appliction link
for i in range(0, len(page_list), 1):
    main_url = url + page_list[i]
    #print(main_url)
    resp = requests.get(main_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    job_title = soup.find("article").find("h1")
    print("Job Title:", job_title.text.strip(), end="\n")

    contact_elts = soup.find("article").find(class_="contact").find_all("div")#.find(string=" Email ")
    #print(contact_elts)
    #print(email.text, end="\n"*2)


    # job_list = soup.find_all("div", class_="job")

    # print(job_list)

    # # # print out all jobs, add 2 new lines @ end of job string

    for job in contact_elts:
        
        #print(job, "\n"*2)
        #print("-------")
        email = job.find("a") # href="/jobs/hbk-strats-developer.html") #href="/jobs/hbk-strats-developer.html")
        #print(email)
        if email != None:
            print(email.text.strip())

    print("\n"*2)
