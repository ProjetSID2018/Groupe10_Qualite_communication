# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017

@author: Cedric

============================================================================"""

import os
import json

"""============================================================================
    basic functions
============================================================================"""
"""
def Contains(pattern, x):
    ''' Is a pattern contained in x string ? '''
    ok = bool(re.search(str(pattern), str(x)))
    return ok
"""
"""============================================================================
    basic json functions
============================================================================"""

path_source_robot = "/var/www/html/projet2018/data/clean/robot/"
path_target = "/var/www/html/projet2018/data/clean/filtering/"

# Import JSON files
data_robot = {}
for doc in os.listdir(path_source_robot):
    for f in os.listdir(path_source_robot + doc + "/"):
        with open(path_source_robot + doc + "/" + f, "r") as file_robot:
            fdict = json.load(file_robot)
        data_robot[f] = fdict
        continue
    continue

## Manipulate
data = [
        {"content": "Caroline est dehors",
         "tf": {"Caroline": 0, "est": 1, "dehors": 2}},
        {"content": "Je viens de pas trop loin",
         "tf": {"Je": 0, "viens": 1, "de": 2, "pas": 3, "trop": 4, "loin": 5}}
]

## Write JSON file
i = 1
for idict in data:
    f = path_target  + "artJT"+ str(i) + "_filtering.json"
    with open(f, "w") as file_out:
        json.dump(idict, file_out)
    i += 1