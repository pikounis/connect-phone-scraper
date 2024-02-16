
import requests
from bs4 import BeautifulSoup

# Replace 'YOUR_URL_HERE' with the actual URL you want to scrape
url = 'https://connectphone.eu/product/e-sim-unlimited-data-in-greece/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
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
    country_name = country_element.text.strip() if country_element else 'Information not found'

    # Initialize a list to hold the scraped data
    scraped_data = []

    # Find all 'li' elements with class 'variable-item'
    for li in soup.select('li.variable-item'):
        # Extract the desired information
        duration = li.find('span', class_='variable-item-span').text.strip()
        data = li.find('span', class_='variation_data').text.strip()
        price = li.find('span', class_='variation_price').text.strip()

        # Append the information to the list as a dictionary
        scraped_data.append({
            'country': country_name,  # Now correctly includes the country name
            'duration': duration,
            'data': data,
            'price': price
        })

    # Print or use the scraped data as needed
    for item in scraped_data:
        print(item)
else:
    print(f"Failed to fetch the webpage: HTTP {response.status_code}")
