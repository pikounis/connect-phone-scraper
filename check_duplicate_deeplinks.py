import json

# Path to the JSON file
json_file_path = 'deeplinks.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

entry_count = len(data)
print(f"There are {entry_count} entries in the JSON file.")

# Dictionary to count occurrences of each link
link_counts = {}

# List to keep track of duplicates
duplicates = []

# Iterate through each item in the data
for item in data:
    link = item["link"]
    # Count occurrences of each link
    if link in link_counts:
        link_counts[link] += 1
    else:
        link_counts[link] = 1

# Identify duplicates based on link_counts
for link, count in link_counts.items():
    if count > 1:
        duplicates.append(link)

# Check and display duplicates
if duplicates:
    print("Duplicate links found:")
    for dup in duplicates:
        print(dup)
else:
    print("No duplicate links found.")
