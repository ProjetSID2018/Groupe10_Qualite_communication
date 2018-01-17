# -*- coding: utf-8 -*-
# Groupe 10
# Pierrick HERVE
# V1 :
from parser_v1 import activation
import g4_new_gorafi_v1 as g4_gora
import pytest
import sys
from io import StringIO


@pytest.fixture()
def setUp():
    newspaper = 'LeGorafi/'
    rss_function = g4_gora.recovery_new_article_lg
    return activation(rss_function, newspaper)


"""
exceptions are treated
"""
def test_activation1(setUp):
     with pytest.raises(Exception):
         # save the standard output
         old_stdout = sys.stdout
         # define the new output
         result = StringIO()
         sys.stdout = result
     
         # call the function to test
         newspaper = 'LeGorafi/'
         rss_function = g4_gora.recovery_new_article_lg
         activation(rss_function, newspaper)
 
         # get back the standard output
         sys.stdout = old_stdout
         # we get the content of the output
         result_string = result.getvalue()
         assert result_string == 'exception\n'
       
        
"""
the message "<newspaper_name> OK" is printed
"""
def test_activation2(setUp):
    # save the standard output
    old_stdout = sys.stdout
    # define the new output
    result = StringIO()
    sys.stdout = result
    
    # call the function to test
    newspaper = 'LeGorafi/'
    rss_function = g4_gora.recovery_new_article_lg
    activation(rss_function, newspaper)

    # get back the standard output
    sys.stdout = old_stdout
    # we get the content of the output
    result_string = result.getvalue()
    assert result_string == 'LeGorafi/\n'
    

