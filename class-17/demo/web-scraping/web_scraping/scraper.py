import requests

from bs4 import BeautifulSoup

URL = "https://www.bayt.com/en/jordan/jobs/python-jobs/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

all_results = soup.find('div', id='results_inner_card')
# print(type(all_results))

all_jobs = all_results.find_all('li', class_='has-pointer-d')
# print(len(all_jobs))

# print(all_jobs[0])

# title = all_jobs[0].find('a').text.strip()
# company = all_jobs[0].find('b').text.strip()
# desc = all_jobs[0].find('p').text.strip()

# print(title)
# print(company)
# print(desc)


all_jobs_clean = []

for job in all_jobs:
    title = job.find('a').text.strip()
    company = job.find('b').text.strip()
    desc = job.find('p').text.strip()
    clean_job = {'title':title, 'company':company, 'desc':desc}
    all_jobs_clean.append(clean_job)

print(all_jobs_clean)



# Write results to json file
import json

file_content = json.dumps(all_jobs_clean)
with open('all_jobs.json', 'w') as file:
    file.write(file_content)