# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:51:08 2024

@author: Abram Nothnagle
"""

import json

# Opening JSON file
with open('example_2.json') as json_file:
    #Load JSON data from file as a dictionary
    data = json.load(json_file)
    
    #View the data like a nested dictionary (hash)
    print(data['quiz']['sport']['q1']['options'])
    print(data)
    
    #Format the json dictionary to read like a JSON file
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)

#Write JSON to file
with open('demo_result.json', 'w') as fp:
    json.dump(data, fp)

#Just to view that the JSON file was written correctly
with open('demo_result.json') as json_file2:
    data2 = json.load(json_file2)
    #Format the json dictionary to read like a JSON file
    formatted_json2 = json.dumps(data2, indent=4)
    print(formatted_json2)