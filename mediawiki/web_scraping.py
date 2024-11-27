import xml.etree.ElementTree as ET
import re
import pandas as pd

def extract_wikitable_from_xml(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Find the content with the MediaWiki table
    content = root.find(".//text").text
    
    # Extract the table using regex
    table_pattern = r'\{\|(.*?)\|\}'
    table_match = re.search(table_pattern, content, re.DOTALL)
    
    if table_match:
        return table_match.group(0)
    else:
        return None

def parse_wikitable(table_content):
    rows = table_content.split('|-')
    headers = []
    data = []
    
    for row in rows[1:]:  # Skip the first element as it's usually empty
        cells = re.findall(r'\|(.*?)(?=\||$)', row, re.DOTALL)
        cells = [cell.strip() for cell in cells]
        
        if not headers:
            headers = cells
        else:
            data.append(cells)
    
    return headers, data

def wikitable_to_dataframe(xml_file):
    table_content = extract_wikitable_from_xml(xml_file)
    if table_content:
        headers, data = parse_wikitable(table_content)
        df = pd.DataFrame(data, columns=headers)
        return df
    else:
        return None

# Usage
xml_file = '/scratch/gpfs/DANQIC/jz4391/wikiextractor-fork/output_folder/334394.xml'
df = wikitable_to_dataframe(xml_file)

if df is not None:
    print(df)
else:
    print("No table found in the XML file.")