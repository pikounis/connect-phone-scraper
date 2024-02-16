import requests
from bs4 import BeautifulSoup
import json

# Replace 'YOUR_URL_HERE' with the actual URL you want to scrape
url = 'https://connectphone.eu/product/e-sim-unlimited-data-in-greece/'

# Send a GET request to the URL
response = requests.get(url)

# Prepare the result dictionary
result = {
    "country": "",
    "url": url,
    "packages": []
}

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the outer <div> element with the specified classes and then find the inner <div>
    outer_div = soup.find('div',
                          class_='elementor-element elementor-element-832a17e elementor-widget elementor-widget-heading')
    inner_div = outer_div.find('div', class_='elementor-widget-container') if outer_div else None

    # Within the inner <div>, find the <h2> element and extract its text
    country_element = inner_div.find('h2',
                                     class_='elementor-heading-title elementor-size-default') if inner_div else None
    result["country"] = country_element.get_text(strip=True) if country_element else 'Information not found'

    # Find all 'li' elements with class 'variable-item' and extract package details
    for li in soup.select('li.variable-item'):
        duration = li.find('span', class_='variable-item-span').text.strip()
        data = li.find('span', class_='variation_data').text.strip()
        price_text = li.find('span', class_='variation_price').text.strip()

        # Assuming the price is always followed by "€" and convert it to a format without currency symbol
        price = price_text.replace("€", "").strip()
        currency = "EUR"  # Since we're assuming "€" is always the currency

        # Append the package information to the packages list
        result["packages"].append({
            "data": data,
            "duration": duration,
            "price": price,
            "currency": currency
        })

    # Save the result to a JSON file with UTF-8 encoding
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Data has been saved to result.json")
else:
    print(f"Failed to fetch the webpage: HTTP {response.status_code}")
