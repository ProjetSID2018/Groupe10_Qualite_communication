# -*- coding: utf-8 -*-

from g4_utils_v32 import get_hash, already_exists,add_to_index

"""

Test function already_exists:

 if an article already exist the function already_exists return true or false. 

"""


def test_already_exists():


    #creation hash_text.csv file
   
    hashtext = open("hash_text.csv", "w")
    add_to_index('28/10/2018','example text','newpaper test')

    assert already_exists('28/10/2018','example text','newpaper test') == True

    assert already_exists('15/10/2018','example text','newpaper test') == False

    

    