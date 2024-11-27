import json

# Read the original JSON file
with open('wiki_AJ.json', 'r') as file:
    data = json.load(file)

# Filter the entries
filtered_entries = [
    {
        'id': entry['id'],
        'revid': entry['revid'],
        'url': entry['url'],
        'title': entry['title'],
        'tables': entry['tables']
    }
    for entry in data['entries']
    if entry['tables'] == [] and "Demographics" not in entry['title']
]

# Create a new dictionary with the filtered entries
filtered_data = {'entries': filtered_entries}

# Write the filtered data to a new JSON file
with open('filtered_AJ.json', 'w') as file:
    json.dump(filtered_data, file, indent=2)

print("Filtering complete. Results saved to 'filtered_AJ.json'.")