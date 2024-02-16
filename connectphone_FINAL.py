import requests
from bs4 import BeautifulSoup
import json

# Load URLs and countries from links_and_titles.json
with open('deeplinks.json', 'r', encoding='utf-8') as file:
    links_and_titles = json.load(file)

# Initialize a list to hold the results for all countries
all_results = []
counter = 0

# Iterate over each entry in the loaded JSON
for entry in links_and_titles:
    url = entry.get("link", "")
    print(f"{counter}. Processing: {url}")  # Log the current URL being processed

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the country name and packages as before
            outer_div = soup.find('div', class_='elementor-element elementor-element-832a17e elementor-widget elementor-widget-heading')
            inner_div = outer_div.find('div', class_='elementor-widget-container') if outer_div else None
            country_element = inner_div.find('h2', class_='elementor-heading-title elementor-size-default') if inner_div else None
            country_name = country_element.get_text(strip=True) if country_element else entry.get("country", "Information not found")

            packages = []
            for li in soup.select('li.variable-item'):
                try:
                    duration = li.find('span', class_='variable-item-span').text.strip()
                    data = li.find('span', class_='variation_data').text.strip()
                    price_text = li.find('span', class_='variation_price').text.strip()
                    price = price_text.replace("€", "").strip()
                    currency = "EUR"

                    packages.append({
                        "data": data,
                        "duration": duration,
                        "price": price,
                        "currency": currency
                    })
                except AttributeError as e:
                    print(f"Error processing package data in {url}: {e}")

            # Append the result for this entry
            all_results.append({
                "country": country_name,
                "url": url,
                "packages": packages
            })
        else:
            print(f"Failed to fetch the webpage for {url}: HTTP {response.status_code}")
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
    counter += 1

# Save all results into results.json
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=4)

print("Data has been saved to results.json")
