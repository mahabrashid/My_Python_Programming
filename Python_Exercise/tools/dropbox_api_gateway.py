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


# Add OAuth2 access token here.
# You can generate one for yourself in the App Console.
# See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
ACCESS_TOKEN = None
dbx = None

# Uploads contents of LOCALFILE to Dropbox
def backup(LOCALFILE, BACKUPPATH):  ##### modified to include the parameters    #####
    if(LOCALFILE is (None or "") or BACKUPPATH is (None or "")):
        sys.exit("invalid parameters, please enter valid LOCALFILE and BACKPATH")
    
    ##### modified to include invalid object check    #####
    if(dbx is None):
        sys.exit("dropbox object is set to None, please initiate dropbox object first.")
        
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()
        
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
    '''
    if(dbx is None):
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
    '''
    for entry in dbx.files_list_folder('').entries:
        print(entry.name)

def initiate_drpbx_obj():
    global ACCESS_TOKEN
    with open("./data_files/do_not_commit.txt") as f:
        for line in f:
            ACCESS_TOKEN = line
    # Check for an access token
    if (len(ACCESS_TOKEN) == 0 or ACCESS_TOKEN == '' or ACCESS_TOKEN is None):
        sys.exit("ERROR: Looks like you didn't add your access token. ")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    global dbx
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an "
            "access token from the app console on the web.")

    
def no_such_file_on_dropbox(err):
    '''
    return True/False for a file's existence on dropbox
    @param err: ApiError object
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

##################################################
### end of extended code                     ###
##################################################

if __name__ == '__main__':
########################################################
###   extended code to test functionality       ###
########################################################
    initiate_drpbx_obj()

    ## Print all dropbox files
#     print_my_drpbx_files()
    
    ## Create a backup of the current settings file
#     backup(r"C:\Users\marashid\Documents\Personal_Stuff\Personal Training and Development\Python\Python_Exercise\tools\sample_CSVs\SimpleCSVSample.csv", "/SimpleCSVSample.csv")
    
    try:
        print(type(get_my_drpbx_file_metadata("/SimpleCSVSample.csv")))
    except ApiError as err:
        if(no_such_file_on_dropbox(err)):
            print("specified file is not found on Dropbox, check the file name and path are correct.")
    except ApiError as err:
        print("some ApiError has occurred which excludes 'file not found on dropbox'")
        print("error returned from ApiError: " + err.error)
        print("error message: " + err.user_message_text)
    except Exception as exp:
        sys.exit("program is exiting due to unknown exception...")

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