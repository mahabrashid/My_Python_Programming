'''
Created on 1 Dec 2017

@author: marashid
'''
import os.path

def get_metadata_for_single_file(file_path):
    '''
    returns the metadata for a file in the form of a dictionary
    '''
    abs_file_path = os.path.abspath(file_path)
    
    a_time = os.path.getatime(abs_file_path)
    c_time = os.path.getctime(abs_file_path)
    m_time = os.path.getmtime(abs_file_path)
    size = os.path.getsize(abs_file_path)
        
    return {"path":abs_file_path, "access_time":a_time, "create_time":c_time, "modify_time":m_time, "size":size}

'''
# Test
print(get_metadata_for_single_file("test_file.txt"))
'''