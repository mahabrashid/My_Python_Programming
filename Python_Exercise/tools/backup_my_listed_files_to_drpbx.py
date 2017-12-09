'''
Created on 2 Dec 2017

@author: marashid
'''
import sys
from _datetime import datetime, timedelta

from dropbox.exceptions import ApiError

import csv_reader
import file_metadata_reader
import dropbox_api_gateway

##### Function Definitions #####
def _get_file_metadata(file, required_metadata):
    '''
    retuns ONLY the required_metadata for a given file
    
    @param file: str :the file to enquire a metadata for
    @param required_metadata :str :metadata required for the program
    '''
    loc_file_meta_data = (file_metadata_reader.get_metadata_for_single_file(file))
#     print(datetime.fromtimestamp(loc_file_meta_data['modify_time']))
    metadata = datetime.fromtimestamp(loc_file_meta_data[required_metadata])
    return metadata

def _get_drpbx_file_metadata(file, required_metadata):
    '''
    retuns ONLY the required_metadata for a given file
    
    @param file: str :the file to enquire a metadata for
    @param required_metadata :str :metadata required for the program
    '''
    drpbx_file_meta_data = dropbox_api_gateway.get_my_drpbx_file_metadata(file)
    metadata = drpbx_file_meta_data[required_metadata]
    return metadata

def _get_leading_time(loc_modtime, drpbx_modtime):
    '''
    the dropbox server time will always be ahead of local time as uploading file from client will take a few seconds or minutes
    we will ignore updates in less than 5 hours, so add 5 hours to the local modify time
    '''
    loc_modtime_added_5hrs = loc_modtime + timedelta(hours=5)
    
    if(loc_modtime > drpbx_modtime):
        return loc_modtime
    ## ignore dropbox lead time if it's less than 5 hours
    elif(drpbx_modtime > loc_modtime_added_5hrs):        
        return drpbx_modtime
    else:
        return None
##### End of Function Definitions #####

## initiate the dropbox object
dropbox_api_gateway.initiate_drpbx_obj()

## read all Local files and their corresponding dropbox locations from a csv file
my_backup_files_list = csv_reader.read_csv("files_to_backup_test.csv")

## now iterate through each item in the list and perform operations
for record in my_backup_files_list:
    print("="*50)
    local_file = record['LocalFile']    ## local file path with the file at the end of the path
    backup_file = record['BackUpPath']   ## corresponding dropbox file path with the file at the end of the path
    print("file to backup: " + local_file)
    print("dropbox backup location: " + backup_file)
    
    ## get the modified time for both local file and server file 
    loc_file_modified_time = _get_file_metadata(local_file, "modify_time")    ## get the local file's modify_time
    print("local file modify_time: " + str(loc_file_modified_time))
    try:
        drpbx_file_modified_time = _get_drpbx_file_metadata(backup_file, "modify_time")   ## get the backup file's modify_time
        print("dropbox file server_modified time: " + str(drpbx_file_modified_time))
    except ApiError as err:
        ## if the file doesn't exist on dropbox, we will create the file for first time
        if(dropbox_api_gateway.no_such_file_on_dropbox(err)):
            print("specified file is not found on Dropbox, creating dropbox file {}...".format(backup_file))
            dropbox_api_gateway.backup(local_file, backup_file)
        else:
            print("error returned from ApiError: " + err.error)
            print("error message: " + err.user_message_text)
    ## if any othe error occurs, system should exit with an error
    except Exception as exp:
        sys.exit("program is exiting due to unknown exception...")
    
    ## find out whether local file was modified since the server's last update, or vice-versa ignoring the last 5 hours update on dropbox
    leading_time = _get_leading_time(loc_file_modified_time, drpbx_file_modified_time)
    if(leading_time == loc_file_modified_time):
        print("local file is ahead of server, uploading latest local file to dropbox...")
        try:
            dropbox_api_gateway.backup(local_file, backup_file)
        except ApiError as err:
            if(dropbox_api_gateway.no_such_file_on_dropbox(err)):
                print("specified file is not found on Dropbox, check the file name and path are correct.")
        except ApiError as err:
            print("error returned from ApiError: " + err.error)
            print("error message: " + err.user_message_text)
        except Exception as exp:
            sys.exit("program is exiting due to unknown exception...")    
    
    elif(leading_time == drpbx_file_modified_time):
        print("dropbox file is ahead of the local copy, downloading latest file from dropbox...")
        print("***yet to implement***")
    else:
        print("both files are same (ignoring updates in last 5 hours). No upload/download has taken place.")