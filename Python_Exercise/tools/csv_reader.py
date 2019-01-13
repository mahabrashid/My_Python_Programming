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

def read_csv(csv_file_str, comment_char='#'):
    """ will read a csv file with or without comments from a str input and comment; optionally a character defining comments on the csv file"""
    
#     print(comment_char)
    _records = []   #to build a list of records in iteration, each with an OrderedDict object with key, value
    with open(csv_file_str, newline='') as orig_csv_file:
#         print(type(orig_csv_file))
#         print(dir(orig_csv_file))
        
        csv_reader = csv.DictReader(ignore_comments_in_csvfile(orig_csv_file, comment_char))
#         print(csv_reader.fieldnames)
         
        for row in csv_reader:  #iterate through the stream
#             print(row)
#             print(row['Year'])
#             print(row['Make'])
#             print(row['Model'])
            _records.append(row)    
        return _records

def ignore_comments_in_csvfile(orig_csv_file, comment_char):
    """ store each line without a comment as an entry into a lists, thus strip out all comments from the csv file"""
    
    _refined_lines = []
        
    for line in orig_csv_file:
        if(not line.startswith(comment_char)):
#             print("line:", line)
            _refined_lines.append(line)
    
    return _refined_lines


## Test
'''
# records = read_csv("./sample_CSVs/SimpleCSVSample.csv")
records = read_csv(r"C:\Users\mrashid\PersonalSpace\PythonProgramming\Python_Exercise\tools\sample_CSVs\files_to_backup_test.csv") #The r means that the string is to be treated as a raw string, which means all escape codes will be ignored. For an example: '\n' will be treated as a newline character, while r'\n' will be treated as the characters \ followed by n
# print(records)

## following were useful to experiment record
#     print(dir(record))
#     print(records.items())
#     print(record.keys())
#     print(record.values())

for record in records:
    for key in record.keys():
        print(key, end='\t||\t')    # Appends a tab||tab instead of a newline. Keeps on printing on the same for subsequent print(args) statement until a new line is inserted with '\n' or an empty print() statement'
    print() # takes the print statement onto the next line
    
    for value in record.values():
        print(value, end='\t||\t')
    print()
'''