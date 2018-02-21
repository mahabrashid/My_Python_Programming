'''
Created on 3 Jan 2018

@author: marashid
'''
import sys
import win32api

win32api.MessageBox(0, 'You clicked on ' + sys.argv[1], 'Context Menu')