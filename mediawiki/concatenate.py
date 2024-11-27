import os
import glob
import bz2
import xml.etree.ElementTree as ET

# Specify the folder containing XML files
folder_path = '/scratch/gpfs/DANQIC/jz4391/wikiextractor/output_folder'

# Create a root element for the combined XML
root = ET.Element('root')

# Iterate through XML files in the folder
for xml_file in glob.glob(os.path.join(folder_path, '*.xml')):
    tree = ET.parse(xml_file)
    file_root = tree.getroot()
    root.extend(file_root)

# Create an ElementTree object
combined_tree = ET.ElementTree(root)

# Write the combined XML to a temporary file
temp_file = 'combined.xml'
combined_tree.write(temp_file, encoding='utf-8', xml_declaration=True)

# Compress the combined XML file to .bz2
output_file = 'combined.xml.bz2'
with open(temp_file, 'rb') as f_in, bz2.open(output_file, 'wb') as f_out:
    f_out.writelines(f_in)

# Remove the temporary file
# os.remove(temp_file)

print(f"Combined XML files compressed and saved as {output_file}")