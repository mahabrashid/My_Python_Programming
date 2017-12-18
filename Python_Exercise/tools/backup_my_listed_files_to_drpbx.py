'''
Created on 2 Dec 2017

@author: marashid
'''
import os, sys
from _datetime import datetime, timedelta
import logging

from dropbox.exceptions import ApiError

import csv_reader
import file_metadata_reader
import dropbox_api_gateway
from my_logging import MyFileHandler

##### Function Definitions #####
def _get_file_metadata(_local_file, required_metadata):
    '''
    retuns ONLY the required_metadata for a given _local_file
    
    @param _local_file :str -the _local_file to enquire a metadata for
    @param required_metadata :str -metadata required for the program
    '''
    try:
        loc_file_meta_data = (file_metadata_reader.get_metadata_for_single_file(_local_file))
    except Exception as exp:
        logging.error("Couldn't get metadata for the local _local_file {} due to following exception: {}".format(_local_file, exp.__str__()))
        print("Couldn't get metadata for the local _local_file {} due to following exception: {}".format(_local_file, exp.__str__()))
        return None
        
#     print(datetime.fromtimestamp(loc_file_meta_data['modify_time']))
    metadata = datetime.fromtimestamp(loc_file_meta_data[required_metadata])
    return metadata

def _get_drpbx_file_metadata(_backup_file, required_metadata, _local_file):
    '''
    retuns ONLY the required_metadata for a given _backup_file, if the file doesn't exist on the server then create it
    
    @param _backup_file :str -the _backup_file to enquire a metadata for
    @param required_metadata :str -metadata required for the program
    '''
    try:
        drpbx_file_meta_data = dropbox_api_gateway.get_my_drpbx_file_metadata(_backup_file)
    
    except ApiError as err:
        ## if the _backup_file doesn't exist on dropbox, we will create the _backup_file for first time
        if(dropbox_api_gateway.no_such_file_on_dropbox(err)):
            logging.warn("specified _backup_file is not found on Dropbox, creating dropbox _backup_file {}...".format(_backup_file))
            print("specified _backup_file is not found on Dropbox, creating dropbox _backup_file {}...".format(_backup_file))
            dropbox_api_gateway.backup(_local_file, _backup_file)
        else:
            logging.error("error returned from ApiError: " + err.error.__str__())
            print("error returned from ApiError: " + err.error.__str__())
        return None
    
    except Exception as exp:
        logging.error("Couldn't get metadata for the dropbox path {} due to following exception: {}".format(_backup_file, exp.__str__()))
        print("Couldn't get metadata for the dropbox path {} due to following exception: {}".format(_backup_file, exp.__str__()))
        return None
    
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
    
def _backup_local2_drpbx(_local_path, _backup_path):
    ## lets strip out any trailing \ from local path
    if _local_path.endswith(os.path.sep):
        print("truncating separator at the end of local path")
        _local_path = _local_path.strip(os.path.sep) ## removes any leading and trailing character given in param until reaching a character not in the param
    ## lets strip out any trailing / from local path
    if _backup_path.endswith("/"):
        print("truncating separator at the end of dropbox path")
        _backup_path = _backup_path[:-1] ## as for backup path, removing the leading / lead to pattern error, so we only want to remove the trailing / if there's one
        
    ## if local file is a directory, we want to dig into that directory and append the relative path to dropbox location to create same dir structure
    if (os.path.isdir(_local_path)):
        for filename in os.listdir(_local_path):
            newlocal_path = os.path.join(_local_path, filename)
            newbackup_path = _backup_path + "/" + filename
                    
            _backup_local2_drpbx(newlocal_path, newbackup_path)
    else:
        print("local path: {}\nbackup path: {}".format(_local_path, _backup_path))
    
        ## get the modified time for both local file and server file 
        loc_file_modified_time = _get_file_metadata(_local_path, "modify_time")    ## get the local file's modify_time
        logging.debug("local file modify_time: " + str(loc_file_modified_time))
        print("local file modify_time: " + str(loc_file_modified_time))
        if loc_file_modified_time is None:
            return    ## do not execute rest of the code, go to the next record
         
        drpbx_file_modified_time = _get_drpbx_file_metadata(_backup_path, "modify_time", _local_path)   ## get the backup file's modify_time, if doesn't exist create it on the server
        logging.debug("dropbox file server_modified time: " + str(drpbx_file_modified_time))
        print("dropbox file server_modified time: " + str(drpbx_file_modified_time))
        if drpbx_file_modified_time is None:
            return    ## do not execute rest of the code, go to the next record
                
        ## find out whether local file was modified since the server's last update, or vice-versa ignoring the last 5 hours update on dropbox
        leading_time = _get_leading_time(loc_file_modified_time, drpbx_file_modified_time)
        if(leading_time == loc_file_modified_time):
            logging.info("local file is ahead of server, uploading latest local file to dropbox...")
            print("local file is ahead of server, uploading latest local file to dropbox...")
            try:
                dropbox_api_gateway.backup(_local_path, _backup_path)
             
            except ApiError as err:
                if err.user_message_text:
                    logging.error(err.user_message_text + ", cannot backup {} to {}".format(_local_path, _backup_path))
                    print(err.user_message_text + ", cannot backup {} to {}".format(_local_path, _backup_path))
        
            except Exception as exp:
                logging.error(exp.__str__() + ", cannot backup {} to {}".format(_local_path, _backup_path))    
                print(exp.__str__() + ", cannot backup {} to {}".format(_local_path, _backup_path))    
         
        elif(leading_time == drpbx_file_modified_time):
            logging.info("dropbox file is ahead of the local copy, downloading latest file from dropbox...(***yet to implement***)")
            print("dropbox file is ahead of the local copy, downloading latest file from dropbox...(***yet to implement***)")
         
        else:
            logging.info("both files are same (ignoring updates in last 5 hours). No upload/download has taken place.")
            print("both files are same (ignoring updates in last 5 hours). No upload/download has taken place.")
    
##### End of Function Definitions #####

## enable logging
my_logfile_handler = MyFileHandler()
logging.basicConfig(filename=my_logfile_handler.baseFilename, level=logging.INFO,
                        format='%(asctime)s %(module)s.%(funcName)s line:%(lineno)s: %(levelname)-8s [%(process)d] %(message)s')

## initiate the dropbox object
dropbox_api_gateway.initiate_drpbx_obj()

## read all Local files and their corresponding dropbox locations from a csv file
csv_file = "./data_files/files_to_backup_test.csv"
try:
    my_backup_files_list = csv_reader.read_csv(csv_file)    
except Exception as err:
    logging.error("Error reading csv file {}. Program is exiting due to the following error: {}".format(csv_file, err.__str__()))
    sys.exit("Error reading csv file {}. Program is exiting due to the following error: {}".format(csv_file, err.__str__()))

## if any of the key fields is missing in csv file, then program cannot execute further and should terminate
if ('LocalFile' not in my_backup_files_list.__getitem__(0).keys()) or ('BackUpPath' not in my_backup_files_list.__getitem__(0).keys()):
    logging.error("Missing one or more required key fields in the csv file, ensure to have 'LocalFile' and 'BackUpPath' keys in the given csv")
    sys.exit("Missing one or more required key fields in the csv file, ensure to have 'LocalFile' and 'BackUpPath' keys in the given csv")

## now iterate through each item in the list and perform operations
for record in my_backup_files_list:
    print("="*50)
    local_path = record['LocalFile']    ## local file path with the file at the end of the path
    backup_path = record['BackUpPath']   ## corresponding dropbox file path with the file at the end of the path
    logging.debug("CSV local path to backup: " + local_path)
    print("CSV local path to backup: " + local_path)
    logging.debug("CSV dropbox backup path: " + backup_path)
    print("CSV dropbox backup path: " + backup_path)
    
    _backup_local2_drpbx(local_path, backup_path)