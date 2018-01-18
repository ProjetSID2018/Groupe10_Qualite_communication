"""
Group 10 : M.M.
"""
import numpy
import json
import numpy as np
from fonctions_groupe8_a_tester import extract_keys_values

json_data = open('C:/Users/dell/Documents/grp8_pytest/data.json')
data = json.load(json_data)
keys = []
values = []
for k, v in data.items():
    keys.append(k)
    values.append(v)


def test_function():
    assert extract_keys_values(data) == (keys, values)
