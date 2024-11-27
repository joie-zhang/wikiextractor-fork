#!/bin/bash

# Create the output folder if it doesn't exist
mkdir -p output_folder

# List of IDs
ids=(2145410 7599168 8821389 18855244 338344 334394 30873530 2199761 3578923 551330 12446384)

# Loop through each ID and execute the command
for id in "${ids[@]}"; do
    extractPage --id $id /scratch/gpfs/hyen/p-long-proc/wikitable/enwiki-20241001-pages-articles.xml.bz2 > output_folder/${id}.txt
done