'''
Created on 3 Dec 2017

@author: marashid
'''
import os

def convert(LOCALFILEPATH):
    if ("\\" in LOCALFILEPATH):
        print("old LOCALFILEPATH: " + LOCALFILEPATH)
        ## first replace all win path separators \ with nix path separators /
        new_locfile_path = LOCALFILEPATH.replace("\\", "/")
        ## then replace escape all whitespace
        new_locfile_path = new_locfile_path.replace(" ", "\\")
        print("new LOCALFILEPATH: " + new_locfile_path)

## this method uses the 'sep' object (for separator) of os.path, which is of course OS dependent
def easy_convert(LOCALPATH):
    print("old LOCALPATH: " + LOCALPATH)
    ## first replace all win path separators \ with nix path separators /
    new_locfile_path = LOCALPATH.replace(os.path.sep, '/')
    ## then replace escape all whitespace
    new_locfile_path = new_locfile_path.replace(" ", "\\ ")
    print("new LOCALFILEPATH: " + new_locfile_path)

## in order to avoid 'SyntaxError: (unicode error)', the path string is to be prefixed with an 'r' (for raw)
# convert(r"C:\Users\marashid\Documents\Personal_Stuff\Personal\CV\Mahab_Rashid_40.pdf")

## notice the separators are non-win style
easy_convert(r"C:\Users\marashid\Documents\Personal_Stuff\Personal Training and Development\Python")