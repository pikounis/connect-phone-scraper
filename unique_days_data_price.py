import json

# Path to your JSON file
file_path = 'results.json'

# Initialize sets to store unique data volumes and durations
unique_data_volumes = set()
unique_durations = set()
unique_prices = set()

# Load the JSON data from the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    # Assuming the JSON structure includes a list of country entries
    for entry in data:
        packages = entry['packages']
        for package in packages:
            # Add the data volume and duration to the respective sets
            unique_data_volumes.add(package['data'])
            unique_durations.add(package['duration'])
            unique_prices.add(package['price'])

# Convert the sets to sorted lists for better readability
sorted_data_volumes = sorted(list(unique_data_volumes))
sorted_durations = sorted(list(unique_durations))
sorted_prices = sorted(list(unique_prices))

# Print the unique data volumes and durations
print("Unique Data Volumes:", sorted_data_volumes)
print("Unique Durations:", sorted_durations)
# print("Unique Prices:", sorted_prices)

# Sort prices by converting them to float for accurate numerical sorting
sorted_prices = sorted(list(unique_prices), key=lambda x: float(x.replace(',', '.')))

# Print the sorted unique prices in ascending order
print("Unique Prices (ascending):", sorted_prices)


# Optional: Save the unique values to a file or process them further as needed
