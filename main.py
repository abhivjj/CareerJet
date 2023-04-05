import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the job posting website to scrape
URL = 'https://www.example.com/job-postings/'

# Send a GET request to the URL and get the response
response = requests.get(URL)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the job postings on the page
job_postings = soup.find_all('div', class_='job-posting')

# Open a CSV file for writing the job postings data
with open('job_postings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Location', 'Job Description'])

    # Iterate through each job posting and extract relevant data
    for job_posting in job_postings:
        job_title = job_posting.find('h2', class_='job-title').text.strip()
        company = job_posting.find('div', class_='company').text.strip()
        location = job_posting.find('div', class_='location').text.strip()
        job_description = job_posting.find('div', class_='job-description').text.strip()

        # Write the data to the CSV file
        writer.writerow([job_title, company, location, job_description])

# Print a message when the job postings have been scraped and saved to the CSV file
print('Job postings have been scraped and saved to job_postings.csv.')
