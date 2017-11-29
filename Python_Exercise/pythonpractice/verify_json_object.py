'''
Created on 3 Nov 2017

@author: marashid
'''
import json

## function to return an example json object 
def get_example_json_for_test():
    ## json.dumps() serializes a python object to a json object while json.loads() deserializes a json obj to a python object (dictionary)
    return json.dumps({'uid': '056ccb14-bb96-4392-b076-53b56a2240ac', 'sid': 'fKyT5hDZx7bfWMLYfnmYBa_RgF2vj-X2AFnW8GsN2EI', 'url': 'https://35.158.94.126:443/web_api', 'session-timeout': 600, 'api-server-version': '1.1'})

## function to verify if an object is json
def is_json(val):
    try:
        json.loads(val)
    except TypeError: ## json.loads() function raises TypeError for invalid json doc
        return False
    return True

exmpl_json=get_example_json_for_test()

if(is_json(exmpl_json)):
    conv_dict=json.loads(exmpl_json)
    if('sid' in conv_dict):
        print(conv_dict['sid'])
    else:
        print("no 'sid' found in the json doc")
else:
    print("returned value is not a json doc")