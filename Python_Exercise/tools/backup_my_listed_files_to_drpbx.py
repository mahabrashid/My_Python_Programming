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
def _get_file_metadata(file, required_metadata):
    '''
    retuns ONLY the required_metadata for a given file
    
    @param file :str -the file to enquire a metadata for
    @param required_metadata :str -metadata required for the program
    '''
    ## only file path is supported at the moment, so directory path will rejected
    if os.path.isdir(file):
        logging.error("The path in the csv file, {}, is a directory. Please change this to a file and try again.".format(file))
        sys.exit("The path in the csv file, {}, is a directory. Please change this to a file and try again.".format(file))
    
    try:
        loc_file_meta_data = (file_metadata_reader.get_metadata_for_single_file(file))
    except Exception as exp:
        logging.error("Couldn't get metadata for the local file {} due to following exception: {}".format(file, exp.__str__()))
        print("Couldn't get metadata for the local file {} due to following exception: {}".format(file, exp.__str__()))
        return None
        
#     print(datetime.fromtimestamp(loc_file_meta_data['modify_time']))
    metadata = datetime.fromtimestamp(loc_file_meta_data[required_metadata])
    return metadata

def _get_drpbx_file_metadata(file, required_metadata):
    '''
    retuns ONLY the required_metadata for a given file
    
    @param file :str -the file to enquire a metadata for
    @param required_metadata :str -metadata required for the program
    '''
#     print("dropbox path: " + file)
    ## only file path is supported at the moment, so directory path will be rejected
    if os.path.isdir(file):
        logging.error("The path in the csv file, {}, is a directory. Please change this to a file and try again.".format(file))
        sys.exit("The path in the csv file, {}, is a directory. Please change this to a file and try again.".format(file))
    
    try:
        drpbx_file_meta_data = dropbox_api_gateway.get_my_drpbx_file_metadata(file)
    
    except ApiError as err:
        ## if the file doesn't exist on dropbox, we will create the file for first time
        if(dropbox_api_gateway.no_such_file_on_dropbox(err)):
            logging.error("specified file is not found on Dropbox, creating dropbox file {}...".format(backup_file))
            print("specified file is not found on Dropbox, creating dropbox file {}...".format(backup_file))
            dropbox_api_gateway.backup(local_file, backup_file)
        else:
            logging.error("error returned from ApiError: " + err.error.__str__())
            print("error returned from ApiError: " + err.error.__str__())
        return None
    
    except Exception as exp:
        logging.error("Couldn't get metadata for the dropbox path {} due to following exception: {}".format(file, exp.__str__()))
        print("Couldn't get metadata for the dropbox path {} due to following exception: {}".format(file, exp.__str__()))
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
##### End of Function Definitions #####

## enable logging
my_logfile_handler = MyFileHandler()
logging.basicConfig(filename=my_logfile_handler.baseFilename, level=logging.DEBUG,
                        format='%(asctime)s %(module)s.%(funcName)s line:%(lineno)s: %(levelname)-8s [%(process)d] %(message)s')

## initiate the dropbox object
dropbox_api_gateway.initiate_drpbx_obj()

## read all Local files and their corresponding dropbox locations from a csv file
csv_file = "./data_files/files_to_backup.csv"
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
    local_file = record['LocalFile']    ## local file path with the file at the end of the path
    backup_file = record['BackUpPath']   ## corresponding dropbox file path with the file at the end of the path
    logging.debug("file to backup: " + local_file)
    print("file to backup: " + local_file)
    logging.debug("dropbox backup location: " + backup_file)
    print("dropbox backup location: " + backup_file)
    
    ## get the modified time for both local file and server file 
    loc_file_modified_time = _get_file_metadata(local_file, "modify_time")    ## get the local file's modify_time
    logging.debug("local file modify_time: " + str(loc_file_modified_time))
    print("local file modify_time: " + str(loc_file_modified_time))
    if loc_file_modified_time is None:
        continue    ## do not execute rest of the code, go to the next record
    
    drpbx_file_modified_time = _get_drpbx_file_metadata(backup_file, "modify_time")   ## get the backup file's modify_time
    logging.debug("dropbox file server_modified time: " + str(drpbx_file_modified_time))
    print("dropbox file server_modified time: " + str(drpbx_file_modified_time))
    if drpbx_file_modified_time is None:
        continue    ## do not execute rest of the code, go to the next record
           
    ## find out whether local file was modified since the server's last update, or vice-versa ignoring the last 5 hours update on dropbox
    leading_time = _get_leading_time(loc_file_modified_time, drpbx_file_modified_time)
    if(leading_time == loc_file_modified_time):
        logging.info("local file is ahead of server, uploading latest local file to dropbox...")
        print("local file is ahead of server, uploading latest local file to dropbox...")
        try:
            dropbox_api_gateway.backup(local_file, backup_file)
        
        except ApiError as err:
            if err.user_message_text:
                logging.error(err.user_message_text + ", cannot backup {} to {}".format(local_file, backup_file))
                print(err.user_message_text + ", cannot backup {} to {}".format(local_file, backup_file))

        except Exception as exp:
            logging.error(exp.__str__() + ", cannot backup {} to {}".format(local_file, backup_file))    
            print(exp.__str__() + ", cannot backup {} to {}".format(local_file, backup_file))    
    
    elif(leading_time == drpbx_file_modified_time):
        logging.info("dropbox file is ahead of the local copy, downloading latest file from dropbox...(***yet to implement***)")
        print("dropbox file is ahead of the local copy, downloading latest file from dropbox...(***yet to implement***)")
    
    else:
        logging.info("both files are same (ignoring updates in last 5 hours). No upload/download has taken place.")
        print("both files are same (ignoring updates in last 5 hours). No upload/download has taken place.")