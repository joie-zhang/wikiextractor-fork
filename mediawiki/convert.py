import xml.etree.ElementTree as ET
import json
import pandas as pd
from bs4 import BeautifulSoup
import re

def clean_text(text):
    if text is None:
        return ""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text().strip()

def extract_tables(text):
    if text is None:
        return []
    soup = BeautifulSoup(text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    return [pd.read_html(str(table))[0].to_csv(index=False) for table in tables]

def process_page(page):
    title = page.find('title').text if page.find('title') is not None else ""
    ns = page.find('ns').text if page.find('ns') is not None else ""
    page_id = page.find('id').text if page.find('id') is not None else ""
    
    revision = page.find('revision')
    if revision is not None:
        text_elem = revision.find('text')
        text = text_elem.text if text_elem is not None else ""
    else:
        text = ""

    cleaned_text = clean_text(text)
    tables = extract_tables(text)

    return {
        "id": page_id,
        "title": title,
        "ns": ns,
        "text": cleaned_text,
        "tables": tables
    }

def xml_to_json(input_file, output_file):
    context = ET.iterparse(input_file, events=('end',))
    
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for event, elem in context:
            if elem.tag.endswith('page'):
                page_data = process_page(elem)
                json.dump(page_data, jsonl_file, ensure_ascii=False)
                jsonl_file.write('\n')
                elem.clear()

if __name__ == "__main__":
    input_file = '/scratch/gpfs/DANQIC/jz4391/wikiextractor-fork/output_folder/results_by_confederation.xml'  # Replace with the path to your XML file
    output_file = 'output_2.jsonl'
    
    xml_to_json(input_file, output_file)
    print(f"Conversion complete. Output written to {output_file}")