'''
Created on 1 Dec 2017

@author: marashid

Rules typical of "CSV" specifications and implementations are as follows:
- CSV is a delimited data format that has fields/columns separated by the comma character and records/rows terminated by newlines.
- A CSV file does not require a specific character encoding, byte order, or line terminator format.
- A record ends at a line terminator.
- The first record may be a "header", which contains column names in each of the fields (there is no reliable way to tell whether a file does this or not; however, it is uncommon to use characters other than letters, digits, and underscores in such column names).
'''

import csv

def read_csv(csv_file_str):
    _records = []
    with open(csv_file_str, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
#         print(csv_reader.fieldnames)
        
        for row in csv_reader:
#             print(row)            
#             print(row['Year'])
#             print(row['Make'])
#             print(row['Model'])
            _records.append(row)
        
        return _records


## Test
# records = read_csv("./sample_CSVs/SimpleCSVSample.csv")
# records = read_csv(r"C:\Users\marashid\Documents\Personal_Stuff\Personal Training and Development\Python\Python_Exercise\tools\sample_CSVs\SimpleCSVSample.csv")
# 
# for record in records:
#     print(record)
