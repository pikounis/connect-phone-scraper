import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage you want to scrape
url = 'https://connectphone.eu'

# Send a HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find all 'h2' tags with the specific class to extract the text and href attribute
h2_tags = soup.find_all('h2', class_='elementor-heading-title elementor-size-default')

data = []  # List to store the dictionary of country and link

for tag in h2_tags:
    a_tag = tag.find('a')  # Find the 'a' tag within the 'h2' tag
    if a_tag:
        country = a_tag.text.strip()  # Text of the 'a' tag
        link = a_tag['href'].strip()  # href attribute of the 'a' tag
        data.append({"country": country, "link": link})

# Write the data to a JSON file
with open('deeplinks.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been written to deeplinks.json")
