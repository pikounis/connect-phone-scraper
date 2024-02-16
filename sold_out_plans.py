import json

# Load the JSON data from the file
file_path = 'results.json'  # Update this path to your JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over each entry and check for empty packages
countries_with_no_packages = [entry['country'] for entry in data if len(entry['packages']) == 0]

# Print countries with no packages
if countries_with_no_packages:
    print("Countries with no packages:")
    for country in countries_with_no_packages:
        print(country)
else:
    print("All countries have packages.")
