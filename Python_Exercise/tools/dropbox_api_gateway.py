'''
Created on 1 Dec 2017

@author: marashid
'''
"""
Backs up and restores a settings file to Dropbox.
This is an example app for API v2.
"""

import sys

import dropbox
from dropbox.exceptions import ApiError, AuthError
from dropbox.files import WriteMode

import logging


# Add OAuth2 access token here.
# You can generate one for yourself in the App Console.
# See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
ACCESS_TOKEN = None
dbx = None


def no_such_file_on_dropbox(err):
    '''
    return True/False for a file's existence on dropbox
    @param err :ApiError object
    '''    
## following lines were important to experiment how to narrow down to the most specific ApiError in order to take appropriate decision
#     print(err.error)
#     print(type(str(err.error)))         
#     print("LookupError('not_found'" in (str(err.error)))
#     print(dir(err))
#     print(err.__dict__['error'])
#     print(err.__dict__['error'].__class__.__dict__)
#     print(dir(err.__dict__['error'].__dict__['path']))
#     print(err.__dict__['error'].__class__.__dict__['path'].__dict__)
#     print("specified file is not found on Dropbox, check the file name and path are correct.")
    return True if("LookupError('not_found'" in (str(err.error))) else False


def backup(LOCALFILE, BACKUPPATH):  ##### modified to include the parameters    #####
    '''
    Uploads contents of LOCALFILE to Dropbox
    
    While inevitably terminating exceptions be caught here and program killed, other exceptions should be passed to the caller to decide subsequent actions.
    '''
    if(LOCALFILE is (None or "") or BACKUPPATH is (None or "")):
        logging.error("LOCALFILE or BACKUP path is invalid, cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
        print("LOCALFILE or BACKUP path is invalid, cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
        return
    
    ##### modified to include invalid object check    #####
    if(dbx is None):
        logging.error("dropbox object is set to None, please initiate dropbox object first.")
        sys.exit("dropbox object is set to None, please initiate dropbox object first.")
        
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        logging.info("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                logging.error("ERROR: Cannot back up; insufficient space.")
                sys.exit("ERROR: Cannot back up; insufficient space.")
        except Exception as exp:
            if ("The write operation timed out" in str(exp.__str__())):
                if (dbx._timeout < 150):    ## if a timeout occurs, increase the _timeout by 30 seconds and try again until _timeout value reaches 2 minutes
                    logging.debug("Timeout occurred during write operation, increasing the timeout by 30 seconds...")
                    print("Timeout occurred during write operation, increasing the timeout by 30 seconds...")
                    dbx._timeout += 30
                    logging.debug("New timeout value is: " + dbx._timeout.__str__())
                    print("New timeout value is: " + dbx._timeout.__str__())
                    backup(LOCALFILE, BACKUPPATH)
                else:
                    logging.error("Aborting writing attempt after long timeout, could not upload {} to {}".format(LOCALFILE, BACKUPPATH))
                    print("Aborting writing attempt after long timeout, could not upload {} to {}".format(LOCALFILE, BACKUPPATH))
                    
            ## following are some example of how an exception thrown from this method call can be handled by the caller
#             elif err.user_message_text:
#                 logging.error(err.user_message_text + "cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
#                 print(err.user_message_text + "cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
#             else:
#                 logging.error(err.__str__() + "cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
#                 print(err.__str__() + "cannot backup {} to {}".format(LOCALFILE, BACKUPPATH))
        
'''
# Change the text string in LOCALFILE to be new_content
# @param new_content is a string
def change_local_file(new_content):
    print("Changing contents of " + LOCALFILE + " on local machine...")
    with open(LOCALFILE, 'wb') as f:
        f.write(new_content)
'''
                
'''
# Restore the local and Dropbox files to a certain revision
def restore(rev=None):
    # Restore the file on Dropbox to a certain revision
    print("Restoring " + BACKUPPATH + " to revision " + rev + " on Dropbox...")
    dbx.files_restore(BACKUPPATH, rev)

    # Download the specific revision of the file at BACKUPPATH to LOCALFILE
    print("Downloading current " + BACKUPPATH + " from Dropbox, overwriting " + LOCALFILE + "...")
    dbx.files_download_to_file(LOCALFILE, BACKUPPATH, rev)

# Look at all of the available revisions on Dropbox, and return the oldest one
def select_revision():
    # Get the revisions for a file (and sort by the datetime object, "server_modified")
    print("Finding available revisions on Dropbox...")
    entries = dbx.files_list_revisions(BACKUPPATH, limit=30).entries
    revisions = sorted(entries, key=lambda entry: entry.server_modified)

    for revision in revisions:
        print(revision.rev, revision.server_modified)

    # Return the oldest revision (first entry, because revisions was sorted oldest:newest)
    return revisions[0].rev
'''

########################################################
###   extended code to facilitate extra func        ###
########################################################    
def get_my_drpbx_file_metadata(dropbox_file_path):
    '''
    Get the metadata for a given file in dropbox
    example metadata: FileMetadata(name='my cv23.pdf', id='id:CJ_idZ9Oln4AAAAAAAABow', client_modified=datetime.datetime(2014, 5, 14, 22, 16, 29), server_modified=datetime.datetime(2014, 5, 14, 22, 16, 33), rev='2f0d02782059', size=98739, path_lower='/cv stuff/tailored cvs/my cv23.pdf', path_display='/cv stuff/tailored CVs/my cv23.pdf', parent_shared_folder_id=None, media_info=None, sharing_info=None, property_groups=None, has_explicit_shared_members=None, content_hash='6c250b055fbd5f77cb457e99ee60228e1c6c71e417fc5f6abb24ffcd44d5f644')
    @param drop_file_path :str -path to file on dropbox
    
    While inevitably terminating exceptions be caught here and program killed, other exceptions should be passed to the caller to decide subsequent actions.
    '''
    if(dbx is None):
        logging.error("dropbox object is set to None, please initiate dropbox object first.")
        sys.exit("dropbox object is set to None, please initiate dropbox object first.")

    file_metadata = dbx.files_get_metadata(dropbox_file_path)
#     print(dir(file_metadata))
#     print(file_metadata.path_display)
#     print(file_metadata.client_modified)
#     print(file_metadata.server_modified)
#     print(file_metadata.size)
    return {"path":file_metadata.path_display, "modify_time":file_metadata.server_modified, "size":file_metadata.size}
    

def print_my_drpbx_files():
    '''
    print all file names in the dropbox root directory
    
    While inevitably terminating exceptions be caught here and program killed, other exceptions should be passed to the caller to decide subsequent actions.
    '''
    for entry in dbx.files_list_folder('').entries:
        print(entry.name)


def initiate_drpbx_obj():
    '''
    While inevitably terminating exceptions be caught here and program killed, other exceptions should be passed to the caller to decide subsequent actions.
    '''
    global ACCESS_TOKEN
    try:
        accesstoken_file = "./data_files/do_not_commit.txt"
        with open(accesstoken_file) as f:
            for line in f:
                ACCESS_TOKEN = line
    
        # Check for an access token
        if (len(ACCESS_TOKEN) == 0 or ACCESS_TOKEN == '' or ACCESS_TOKEN is None):
            raise RuntimeError("ERROR: Looks like you didn't add your access token. ")
    
        # Create an instance of a Dropbox class, which can make requests to the API.
        logging.debug("Creating a Dropbox object...")
        print("Creating a Dropbox object...")
        global dbx
        dbx = dropbox.Dropbox(ACCESS_TOKEN)
    
        # Check that the access token is valid        
        dbx.users_get_current_account()
        
    except FileNotFoundError as fnferr:
        logging.error(fnferr.strerror + ": " + accesstoken_file)
        sys.exit((fnferr.strerror + ": " + accesstoken_file))
    except RuntimeError as rterr:
        logging.error("Program is exiting due to the following error: " + rterr.__str__())
        sys.exit("Program is exiting due to the following error: " + rterr.__str__())
    except AuthError:
        logging.error("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

##################################################
### end of extended code                     ###
##################################################

if __name__ == '__main__':
########################################################
###   extended code to test functionality       ###
########################################################
    initiate_drpbx_obj()
    
    try:
        ## print metadata for a given dropbox file
        print((get_my_drpbx_file_metadata("/L&D/AWS CSA/section2_notes.docx")))
        print((dbx._timeout))
        
        ## Print all dropbox files
#         print_my_drpbx_files()
    
        ## Create a backup of the current settings file
#         backup(r"C:\Users\marashid\Documents\Personal_Stuff\Personal Training and Development\Python\Python_Exercise\tools\sample_CSVs\SimpleCSVSample.csv", "/SimpleCSVSample.csv")
    
    except ApiError as err:
        if(no_such_file_on_dropbox(err)):
            logging.error("specified file is not found on Dropbox, check the file name and path are correct.")
            print("specified file is not found on Dropbox, check the file name and path are correct.")
    except ApiError as err:
        logging.error("error returned from ApiError: " + err.error.__str__())
        print("error returned from ApiError: " + err.error.__str__())
    except Exception as exp:
        logging.error("program is exiting due to following exception..." + exp.__str__())
        sys.exit("program is exiting due to following exception..." + exp.__str__())

########################################################
###   end of extended code                      ###
########################################################        

'''
    # Change the user's file, create another backup
    change_local_file("updated")
    backup()

    # Restore the local and Dropbox files to a certain revision
    to_rev = select_revision()
    restore(to_rev)

    print("Done!")
'''