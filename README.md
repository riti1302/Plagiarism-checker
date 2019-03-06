# Plagiarism-checker
A simple command line tool to find out whether a pdf is plagiarised from an already existing database or not. 
It finds the strings that match a given pattern. It uses Levenshtein distance to calculate the difference between sequences.
It work on python version 3.0 or higher.

## Requirements
Fuzzywuzzy

              pip3 install fuzzywuzzy
Python-Levenshtein
    
              pip3 install python3-Levenshtein
              
## Usage
The dataset is very large and is zipped in [Dataset](Dataset). For use, clone this repository

              git clone "https://github.com/riti1302/Plagiarism-checker.git"
Navigate to [Dataset](Dataset) and unzip the dataset then run the following command:

              python3 main.py <path/of/the/pdf/file/to/be/checked>
              
To add your own dataset copy all the files in [Dataset](Dataset)
To increase the checking speed, increase the number of threads.

## Output
If the pdf is partially or fully plagiarised - "Copied from <name of the pdf>"
If the pdf is not plagiarised - "Bravo! Original work"
