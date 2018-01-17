# -*- coding: utf-8 -*-

import csv
from g4_utils_v32 import get_hash, already_exists,add_to_index

"""

Test function add_to_index:

 After adding a line in hash_text file, we verify if this line is inserted. 
 
"""

def test_add_to_index():

    text=""
    add_to_index("01/01/01","text01", "01")
    t = get_hash("01/01/01","text01", "01")
#     h=open("hash_text.csv", "r")
    
    with open("hash_text.csv", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            text+=str(row)
    assert t in text
     

     

 

     