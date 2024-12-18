# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:51:08 2024

@author: Abram Nothnagle
"""

import json
import pandas as pd

# Opening JSON file
def testJSONOpen(fileName):
    with open(fileName) as json_file:
        #Load JSON data from file as a dictionary
        data = json.load(json_file)
        
        #View the data like a nested dictionary (hash)
        print(data['quiz']['sport']['q1']['options'])
        print(data)
        
        #Format the json dictionary to read like a JSON file
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
        return data

#Write JSON to file
def testJSONWrite(data):
    with open('demo_result.json', 'w') as fp:
        json.dump(data, fp)

#Just to view that the JSON file was written correctly
def testJSONView(fileName):
    with open(fileName) as json_file2:
        data2 = json.load(json_file2)
        #Format the json dictionary to read like a JSON file
        formatted_json2 = json.dumps(data2, indent=4)
        print(formatted_json2)

'''        
#Test json API
data = testJSONOpen('example_2.json')
testJSONWrite(data)
testJSONView('demo_result.json')
'''

#open and load a JSON file into a Pandas DF
def testPandasJSONOpen(fileName):
    jsonDF = pd.read_json(fileName)
    #print(jsonDF['quiz']['sport'])
    print(jsonDF)
    return jsonDF

#Testing Pandas JSON with multiple types
def testPandasJSONModify(fileName):
    data = testPandasJSONOpen(fileName)
    print(data['data']["Name"])
    
    #Change the name
    if data['data']["Name"] == "Bob":
        data['data']["Name"] = "Steve"
    elif data['data']["Name"] == "Steve":
        data['data']["Name"] = "Bob"
        
    #Update Status:
    if data['data']["Status"][0] == 1:
        for i in range(len(data['data']["Status"])):
            data['data']["Status"][i] = data['data']["Status"][i]*2
    elif data['data']["Status"][0] == 2:
        for i in range(len(data['data']["Status"])):
            data['data']["Status"][i] = i+1
    data.to_json(fileName)
    
    

#Write Pandas JSON DF to file
def testPandasJSONWrite(data, fileName):
    data.to_json(fileName, orient = 'index')

#data = testPandasJSONOpen('example_2.json')
#testPandasJSONWrite(data, 'demo_result2.json')

testPandasJSONModify('json_mod_demo.json')