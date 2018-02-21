'''
Created on 2 Jan 2018

@author: marashid
'''
import sys
import pyperclip

# pyperclip.copy("some data")
# print(pyperclip.paste())
pyperclip.copy(sys.argv[1])